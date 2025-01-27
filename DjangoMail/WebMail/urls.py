from django.urls import path
from rest_framework.routers import DefaultRouter
from WebMail import views

router = DefaultRouter()

urlpatterns = [
    # # 渲染欢迎页，其后的页面跳转由前端负责
    # path('homepage/', views.HomePage, name="homepage"),
    # # 渲染模型介绍页，其后的页面跳转由前端负责
    # path('homepage/model/', views.ModelPage, name="model"),

    # # 身份验证请求
    # path('getIdentity/', views.GetIdentity, name="getIdentity"),

    # # 登录请求
    # path('signin/', views.Signin, name="signin"),

    # # 登出请求
    # path('logout/', views.Logout, name="logout"),

    # 邮件发送功能
    path('sendmails/', views.SendMails, name="sendmails"),

    # 显示配置信息
    path('showconfig/', views.ShowConfig, name='showconfig'),

    # 重置配置信息
    path('resetconfig/', views.ResetConfig, name='resetconfig'),
    
    # 过滤用户等级及分页
    path('filterusers/', views.UsersView.as_view()),

    # # 注册请求
    # path('signup/', views.Signup, name="signup"),

    # # 修改密码请求
    # path('changePwd/', views.ChangePwd, name="changePwd"),

    # # 忘记密码请求
    # path('forgetPwd/', views.ForgetPwd, name="forgetPwd"),

    # # 用户管理数据请求
    # path('userManage/', views.GetUserInfos, name="userManage"),
    # path('generalUserManage/', views.GetGeneralUserInfos, name="generalUserManage"),
    # path('adminManage/', views.GetAdminInfos, name="adminManage"),

    # # 图表相关数据请求
    # path('topCity/', views.GetTopCityInfos, name="topCity"),
    # path('sexNum/', views.GetSexNum, name="sexNum"),
    # path('userCaseStat/', views.GetUserCaseStat, name="userCaseStat"),


    # 以下为对任意模型的增删改查列
    # 关于user的请求：
    # 无参数：get=list all,post=create new
    path('users/', views.UsersViewSet.as_view({'get': 'list', 'post': 'create'})),
    # 有参数：get=retrieve one,put=partial_update one,delete=delete one
    path('users/<int:pk>/', views.UsersViewSet.as_view({'get': 'retrieve', 'put': 'partial_update', 'delete': 'destroy'})),

    # 关于mail的请求
    # 无参数：get=list all,post=create new
    path('mails/', views.MailsViewSet.as_view({'get': 'list', 'post': 'create'})),
    # 有参数：get=retrieve one,put=partial_update one,delete=delete one
    path('mails/<int:pk>/', views.MailsViewSet.as_view({'get': 'retrieve', 'put': 'partial_update', 'delete': 'destroy'})),

    # 关于contacts的请求
    # 无参数：get=list all,post=create new
    path('contacts/', views.ContactsViewSet.as_view({'get': 'list', 'post': 'create'})),
    # 有参数：get=retrieve one,put=partial_update one,delete=delete one
    path('contacts/<int:pk>/', views.ContactsViewSet.as_view({'get': 'retrieve', 'put': 'partial_update', 'delete': 'destroy'})),

    # 关于attachments的请求
    # 无参数：get=list all,post=create new
    path('attachments/', views.AttachmentsViewSet.as_view({'get': 'list', 'post': 'create'})),
    # 有参数：get=retrieve one,put=partial_update one,delete=delete one
    path('attachments/<int:pk>/', views.AttachmentsViewSet.as_view({'get': 'retrieve', 'put': 'partial_update', 'delete': 'destroy'})),

]
