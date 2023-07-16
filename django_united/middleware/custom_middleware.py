import os
if os.path.exists('env.py'):
    import env

class GitHubAppMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_domain = request.get_host()

        if current_domain == os.environ.get('HEROKU_HOSTNAME'):
            os.environ['GITHUB_CLIENT_ID'] = os.environ.get('GITHUB_CLIENT_ID_HEROKU')
            os.environ['GITHUB_CLIENT_SECRET'] = os.environ.get('GITHUB_CLIENT_SECRET_HEROKU')
        elif current_domain == os.environ.get('NAME_DOMAIN'):
            os.environ['GITHUB_CLIENT_ID'] = os.environ.get('GITHUB_CLIENT_ID_UNITEDS')
            os.environ['GITHUB_CLIENT_SECRET'] = os.environ.get('GITHUB_CLIENT_SECRET_UNITEDS')
        else:
            os.environ['GITHUB_CLIENT_ID'] = os.environ.get('GITHUB_CLIENT_ID_LOCAL')
            os.environ['GITHUB_CLIENT_SECRET'] = os.environ.get('GITHUB_CLIENT_SECRET_LOCAL')

        response = self.get_response(request)

        return response