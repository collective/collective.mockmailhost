from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class MyView(BrowserView):

    

    def __call__(self):
        context = self.context
        request = self.request
        id = int(request['id'])
        if id < len(context.messages):
            return context.messages[id]
        return 'NO MESSAGE'
