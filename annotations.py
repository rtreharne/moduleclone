from utils import CanvasSession
from selenium.webdriver.common.by import By
from canvasapi import Canvas
from config import *
import time
import pickle

# import beautifulsoup
from bs4 import BeautifulSoup

def get_urls(submissions):
    return [f"{CANVAS_URL}/courses/{course_id}/gradebook/speed_grader?assignment_id={assignment_id}&student_id={x.user_id}" for x in submissions]


# This function gets the annotations
def get_annotations(session, url):

    session.browser.get(url)
    wait = 0
    while True:

        try:
            session.browser.switch_to.frame('speedgrader_iframe')

            time.sleep(5)

            annotations = []

            html_string = session.browser.page_source
            soup = BeautifulSoup(html_string, 'html.parser')
            annotation_authors = soup.find_all('div', {'class': 'ScreenreaderAnnotation-author'})
            annotation_comments = soup.find_all('div', {'class': 'ScreenreaderAnnotation-root-comment'})

            for author, annotation in zip(annotation_authors, annotation_comments):
                comment = {
                    "author": author.get_text().split(":")[-1],
                    "comment": annotation.get_text().split(":")[-1],
                    "type": "annotation"
                }

                annotations.append(comment)
                  
            session.browser.switch_to.default_content()

            break
        except:
            if wait > 20:
                annotations = []
                break
            else:
                time.sleep(2)
                wait += 2
                continue

    return annotations    

