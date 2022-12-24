from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import models

# Create your views here.


def search_for_user(request):
    if request.method == "GET":
        if "username" in request.GET.keys():
            context = {
                "result":[User.objects.get(username=request.GET["username"])],
            }
            return render(request, "chatting/search.html", context)
        all = lambda e: e if(e.username != request.user.username) else None
        context = {
            "result":map(all,list(User.objects.all())),
        }
        return render(request, "chatting/search.html", context)


def conversation(request, id):
    messages = models.Message.objects.filter(conv = id)
    if len(messages) < 0:
        message = None
    second_user = lambda:models.Conversation.objects.get(id = id).part1 if (models.Conversation.objects.get(id = id).part1 != request.user) else models.Conversation.objects.get(id = id).part2
    context={
        "cnv_id":id,
        "messages":messages,
        "user":request.user,
        "second_user":second_user,
    }
    return render(request, "chatting/conversation.html", context)
    


def loading_conv(request, id):
    if (models.Conversation.objects.filter(part1=request.user, part2=User.objects.get(id=id)).count()) < 1:
        if  (models.Conversation.objects.filter(part1=User.objects.get(id=id), part2=request.user).count()) < 1:
            cnv = models.Conversation(part1=request.user, part2=User.objects.get(id=id))
            cnv.save()
            return redirect(f"/chatting/conversation/{cnv.id}")
        else:
            cnv = models.Conversation.objects.get(part1=User.objects.get(id=id), part2=request.user)
            return redirect(f"/chatting/conversation/{cnv.id}")
    cnv = models.Conversation.objects.get(part1=request.user, part2=User.objects.get(id=id))
    return redirect(f"/chatting/conversation/{cnv.id}")

def conversations(request):
    result = []
    for i in models.Conversation.objects.all():
        if (i.part1 == request.user) or (i.part2 == request.user):
            if models.Message.objects.filter(conv = i).count()<1:
                continue
            
            result.append(i)
    an = lambda e: e.part1 if(e.part1 != request.user) else e.part2
    result = map(an, result)
        
    return render(request, 'chatting/conversations.html', {
        "result":result,
        'user':request.user
    })