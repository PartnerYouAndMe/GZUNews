from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
# Create your views here.
from .models import newsItem
def news_list(request):

    news_all_list=newsItem.newsManage.all()
    paginator=Paginator(news_all_list,10)   #每10页分页
    page_num = request.GET.get('page',1) #获取url的页面参数（GET请求）
    page_of_news=paginator.get_page(page_num)
    current_page_num=page_of_news.number
    range_of_page=[current_page_num-3,current_page_num-2,
                current_page_num-1,current_page_num,
                current_page_num+1,current_page_num+2,
                current_page_num+3]
    # if(range_of_page[3] < 4):
    #     range_of_page=range_of_page[3:]
    
    context={}
    context['aPageNews']=page_of_news.object_list
    context["page_of_news"]=page_of_news
    context['range_of_page']=range_of_page
    context['max_page_num']=paginator.num_pages
    context['max_page_num_3']=paginator.num_pages-3
    return render_to_response('news_list.html',context)

def news_detail(request,news_pk):
    context={}
    context['aNews']=get_object_or_404(newsItem,pk=news_pk)
    return render_to_response('news_detail.html',context)

def introduct(request):
    return render_to_response('introduct.html')