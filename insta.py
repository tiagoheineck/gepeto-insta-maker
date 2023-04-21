import requests

class InstaPostManager():
    graph_url = 'https://graph.facebook.com/v16.0/'

    def post_image(self,caption='', image_url='',instagram_account_id='',access_token=''):
        url = self.graph_url + instagram_account_id + '/media'
        param = dict()
        param['access_token'] = access_token
        param['caption'] = caption
        param['image_url'] = image_url
        response = requests.post(url, params=param)
        response = response.json()
        return response


    def publish_container(self,creation_id = '',instagram_account_id='',access_token=''):
        url = self.graph_url + instagram_account_id + '/media_publish'
        param = dict()
        param['access_token'] = access_token
        param['creation_id'] = creation_id
        response = requests.post(url,params=param)
        response = response.json()
        return response