# Create your views here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from .bot_config import * # import token, confirmation_token and over constants from bot_config.py
from vk_api.utils import get_random_id

"""
Using VK Callback API version 5.5
For more ditalies visit https://vk.com/dev/callback_api
"""

"""
From Django documentation (https://docs.djangoproject.com/en/1.11/ref/request-response/)
When a page is requested, Django automatically creates an HttpRequest object that contains
metadata about the request. Then Django loads the appropriate view, passing the
HttpRequest as the first argument to the view function.
This argiment is <request> in def index(request):

Decorator <@csrf_exempt> marks a view as being exempt from the protection
ensured by the Django middleware.
For cross site request protection will be used secret key from VK
"""
from django.core.files.storage import default_storage
from django.core.files import File
import os


@csrf_exempt #exempt index() function from built-in Django protection
def index(request): #url: https://mybot.mysite.ru/vk_bot/



    # #  Saving POST'ed file to storage
    # # file = request.FILES['myfile']
    # # file_name = default_storage.save(file.name, file)

    # #  Reading file from storage
    # file = default_storage.open(file_name)
    # file_url = default_storage.url(file_name)

    # with open('out.txt', 'w') as f:
    #     file_name = default_storage.save(f.name, f)

    # # print >> f, 'Filename:', filename     # Python 2.x
    #     print('Filename:', file_name    , file=f)

    # print (request.method)
    # module_dir = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, 'baz.txt')
    with open(file_path, 'w') as f:
        f.write('Hello World')
    

    

    if (request.method == "POST"):
        data = json.loads(request.body)# take POST request from auto-generated variable <request.body> in json format

        if (data['secret'] == secret_key):# if json request contain secret key and it's equal my secret key
            if (data['type'] == 'confirmation'):# if VK server request confirmation
                """
                For confirmation my server (webhook) it must return
                confirmation token, whitch issuing in administration web-panel
                your public group in vk.com.

                Using <content_type="text/plain"> in HttpResponse function allows you
                response only plain text, without any format symbols.
                Parametr <status=200> response to VK server as VK want.
                """
                # confirmation_token from bot_config.py
                return HttpResponse(confirmation_token, content_type="text/plain", status=200)
            if (data['type'] == 'message_new'):# if VK server send a message
                # session = vk.Session()
                vk_session = vk_api.VkApi(token=token, v='5.67')

                vk = vk_session.get_api()
                # user_id = data['object']['user_id']

                # token from bot_config.py
                # api.messages.send(access_token = token, user_id = str(user_id), message = "Hello, I'm bot!")
                vk.messages.send(
                        user_id=str(user_id),
                        random_id=get_random_id(),
                        message="Hello, I'm bot!")

                vk.messages.send(
                        user_id=16200,
                        random_id=0,
                        message="Hello, I'm bot!")

                return HttpResponse('ok', content_type="text/plain", status=200)
    else:
        return HttpResponse('see you :)')