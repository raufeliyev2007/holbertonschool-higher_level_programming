#!/usr/bin/python3
"""
Module for fetching posts from an API and processing them into different formats.
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints their titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """
    Fetches all posts and saves id, title, and body into a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Структурируем данные: оставляем только нужные ключи
        structured_data = [
            {'id': p['id'], 'title': p['title'], 'body': p['body']}
            for p in posts
        ]

        # Запись в CSV
        filename = "posts.csv"
        fieldnames = ['id', 'title', 'body']

        with open(filename, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(structured_data)
