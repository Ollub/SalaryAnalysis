import os
from itertools import count
from statistics import mean

import requests

from tools import predict_salary


def get_sj_vacancies(keyword: str, api_key: str):
    """Get list of vacancies from SJ API by keyword for Moscow region"""
    url = 'https://api.superjob.ru/2.0/vacancies'
    vacancies = []
    moscow_id = 4
    headers = {
        'X-Api-App-Id': api_key
    }

    for page in count(0):
        params = {
            'town': moscow_id,
            'keyword': keyword,
            'page': page,
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        sj_data = response.json()
        vacancies.extend(sj_data['objects'])
        if not sj_data['more']:
            break
    return vacancies


def predict_sj_salary(vacancy):
    if vacancy['currency'] != 'rub':
        return None
    return predict_salary(
        salary_from=vacancy['payment_from'], 
        salary_to=vacancy['payment_to']
        )


def analyze_sj_vacancies(keywords: list, api_key: str):
    """Takes list of jobs_descriptions (keywords),
    get list of vacancies for each keyword from SJ
    and returns dictionary with salary analytics (mean salary)
    """
    result = dict()
    for keyword in keywords:
        vacancies = get_sj_vacancies(keyword, api_key)
        salaries = [predict_sj_salary(vacancy) for vacancy in vacancies]
        salaries = [salary for salary in salaries if salary]
       
        result[keyword] = {
            "vacancies_found": len(vacancies),
            "vacancies_processed": len(salaries),
            "average_salary": int(mean(salaries))
        }
    return result