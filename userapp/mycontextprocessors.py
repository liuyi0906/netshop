
def getUserInfo(request):
    return {"suser":request.session.get('user',None)}