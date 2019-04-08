from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView
from Project01.forms import HomeForm, RegisterForm, EditForm, TicketForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
import uuid
import os

# Create your views here.

messages = []  # list storing the chatbot history

bot = ChatBot('Test',
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              logic_adapters=[
                  {
                      'import_path': 'chatterbot.logic.BestMatch',
                      'default_response': 'I am sorry, but I do not understand.',
                      'maximum_similarity_threshold': 0.90

                  }
              ]
              )

path = 'C:/Users/Rohan/Desktop/MS-Django/EP1/Project01/training_files'

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.custom")

# for filename in os.listdir(path):
#     # chats = open('training_files/' + _file, 'r').readlines()
#     filepath = os.path.join(path, filename)
#     f = open(filepath, 'r')
#     chats = f.read()

#     trainer = ListTrainer(bot)
#     trainer.train(chats)


class HomeView(TemplateView):
    template_name = 'Project01/home.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form, 'home_name': 'Home'})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['hello']
            request_bot = text
            messages.append(request_bot)
            response = bot.get_response(request_bot)
            messages.append(response)
        args = {'form': form, 'response': response, 'home_name': 'Home'}
        return render(request, self.template_name, args)

        # def Login(request):
        #     name = 'Chatbot Home'
        #     args = {'bot_name': name, }
        #     return render(request, 'Project01/login.html', args)


class RegisterView(TemplateView):
    template_name = 'Project01/register.html'

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form, 'register_name': 'Register'})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        args = {'form': form, 'register_name': 'Register'}
        return render(request, self.template_name, args)


class ProfileView(TemplateView):
    template_name = 'Project01/profile.html'

    def get(self, request):
        args = {'user': request.user, 'profile_name': 'Profile'}
        return render(request, self.template_name, args)


class ProfileEditView(TemplateView):
    template_name = 'Project01/profile_edit.html'

    def get(self, request):
        form = EditForm(instance=request.user)
        return render(request, self.template_name, {'form': form, 'name': 'Profile Edit'})

    def post(self, request):
        form = EditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')


class PasswordChange(TemplateView):
    template_name = 'Project01/password_change.html'

    def get(self, request):
        form = PasswordChangeForm(user=request.user)
        return render(request, self.template_name, {'form': form, 'name': 'Password Reset'})

    def post(self, request):
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        else:
            return redirect('password_reset')


class AjaxTest(TemplateView):
    template_name = 'Project01/test_view.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        text = "hello sinora!"
        return HttpResponse(self.template.render(text, request))


class HelpDeskView(TemplateView):
    template_name = 'Project01/help-desk.html'

    def get(self, request):
        form = TicketForm()
        return render(request, self.template_name, {'form': form, 'name': 'HelpDesk'})

    def post(self, request):
        form = TicketForm()
        if form.is_valid():
            form.save()
            return redirect('ticket_submitted')


class TicketView(TemplateView):
    template_name = 'Project01/ticket.html'

    def get(self, request):
        return render(request, self.template_name, {'name': 'HelpDesk'})
