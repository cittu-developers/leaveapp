from django.urls import path
from .import views

urlpatterns = [
    path('leavetype/',views.leave_type, name='leave_type'),
    path('leaveduration/',views.LeaveDurationView , name='leave_duration'),
    path('leaveapplication/<id>/',views.LeaveApplicationview , name='leave_application'),
    path('leaveapplicationstatus/',views.LeaveApplicationStatus , name='leave_applicationstatus'),
    path('Leave_list_by_departments/',views.Leave_list_by_departments , name='Leave_list_by_departments'),
    path('leaveresume/',views.LeaveResumptionView , name='leave_resume'),
    path('leave_types_list/',views.leave_types_list, name='leave_types_list'),
    path('recommend_leave/<id>/',views.recommend_leave_application, name='recommend_leave'),
    path('decline_leave/<id>/',views.decline_leave_application, name='decline_leave'),
]    