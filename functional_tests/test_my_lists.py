from django.conf import settings
from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY, get_user_model
User = get_user_model()

from django.contrib.sessions.backends.db import SessionStore
from .base import FunctionalTest
from .server_tools import create_session_on_server
from .management.commands.create_session import create_pre_authenticated_session


class MylistsTest(FunctionalTest):

    def create_pre_authenticated_session(self, email):
        if self.against_staging:
            session_key = create_session_on_server(self.server_host, email)
        else:
            session_key = create_pre_authenticated_session(email)
        ## 为了设定cookie, 我们先访问网站
        ## 而404页面是加载最快的
        self.browser.get(self.server_url+"/404_no_such_url/")
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session_key,
            path='/',
        ))

    def test_logged_in_user_lists_are_saved_as_my_lists(self):
        # 伊迪丝是已登录用户
        self.create_pre_authenticated_session('edith@example.com')

        # 她访问首页, 新建一个清单
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Reticulate splines\n')
        self.get_item_input_box().send_keys('Immanentize eschaton\n')
        first_list_url = self.browser.current_url

        # 她第一次看到My Lists链接
        self.browser.find_element_by_link_text('My Lists').click()

        # 她看到这个页面中有她创建的清单
        # 而且清单根据第一个待办事项命名
        self.browser.find_element_by_link_text('Reticulate splines').click()
        self.assertEqual(self.browser.current_url, first_list_url)

        # 她决定再建一个清单试试
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Click cows\n')
        second_list_url = self.browser.current_url

        # 在My List页面, 这个新建的清单也显示出来了
        self.browser.find_element_by_link_text('My Lists').click()
        self.browser.find_element_by_link_text('Click cows').click()
        self.assertEqual(self.browser.current_url, second_list_url)

        # 她退出后, My Lists链接不见了
        self.browser.find_element_by_id('id_logout').click()
        self.assertEqual(
            self.browser.find_elements_by_link_text('My lists'),
            []
        )