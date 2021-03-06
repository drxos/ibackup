# @Author: drxos
# @Date:   Friday, May 6th 2016, 6:03:28 pm
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   sadjad
# @Last modified time: 2016-05-19T07:35:48+01:00
# @License: Copyright (c) Foton IT, All Right Reserved



from django.conf.urls import url
from django.core.urlresolvers import reverse

from . import  views


urlpatterns = [
	# --------------------------------------------------------------------------
	url(
		regex = r'^bachelors/$',
		view = views.BachelorListView.as_view(),
		name='bachelor-list'
	),
	url(
		regex = r'^bachelor/create/$',
		view = views.BachelorCreateView.as_view(),
		name='bachelor-add'
	),
	url(
		regex = r'^bachelor/(?P<slug>[-\w]+)/update/$',
		view = views.BachelorUpdateView.as_view(),
		name='update-bachelor'
	),
	url(
		regex = r'^bachelor/(?P<slug>[-\w]+)/$',
		view = views.BachelorDetailView.as_view(),
		name='detail-bachelor'
	),
	url(
		regex = r'^(?P<slug>[-\w]+)/details/semester/create/$',
		view = views.SemesterCreateView.as_view(),
		name='semester-bachelor-add'
	),
	url(
		regex = r'^bachelor/(?P<slug>[-\w]+)/details/semester/(?P<pk>[-\w]+)/lecture/create/$',
		view = views.LectureCreateView.as_view(),
		name='bachelor-lecture-add'
	),
	url(
		regex = r'^master/(?P<slug>[-\w]+)/details/semester/(?P<pk>[-\w]+)/lecture/create/$',
		view = views.MasterLectureCreateView.as_view(),
		name='master-lecture-add'
	),
	url(
		regex = r'^bachelor/(?P<program_slug>[-\w]+)/lecture/(?P<pk>[-\w]+)/update/$',
		view = views.LectureUpdateView.as_view(),
		name='bachelor-lecture-update'
	),
	url(
		regex = r'^master/(?P<program_slug>[-\w]+)/lecture/(?P<pk>[-\w]+)/update/$',
		view = views.MasterLectureUpdateView.as_view(),
		name='master-lecture-update'
	),

	url(
		regex = r'^$',
		view = views.ProgramListView.as_view(),
		name='program-list'
	),

	url(
		regex = r'^(?P<slug>[-\w]+)/program/courses/$',
		view = views.ProgramDetailView.as_view(),
		name='program-courses'
	),
	url(
		regex = r'^(?P<slug>[-\w]+)/program/students/$',
		view = views.AllianzaStudentByProgram.as_view(),
		name='program-student'
	),
	url(
		regex = r'^students/(?P<pk>[-\w]+)/status/$',
		view = views.ActivateRegistredView.as_view(),
		name='student-status'
	),
	
	url(
		regex = r'^(?P<slug>[-\w]+)/program/courses/registration/$',
		view = views.AllianzaStudentCreateView.as_view(),
		name='allianza-registration'
	),
	url(
		regex = r'^(?P<slug>[-\w]+)/program/courses/update/(?P<pk>[-\w]+)/student/$',
		view = views.AllianzaStudentUpdateView.as_view(),
		name='update-student'
	),
	url(
		regex = r'^(?P<slug>[-\w]+)/program/courses/registration/(?P<pk>[-\w]+)/registration/$',
		view = views.AllianzaRegistredCreateView.as_view(),
		name='registration'
	),

	url(
		regex = r'^registration/list/$',
		view = views.AllianzaRegistredListView.as_view(),
		name='registration-list'
	),

	url(
		regex = r'^(?P<slug>[-\w]+)/enroll-program/$',
		view = views.StudentEnrollProgramView.as_view(),
		name = 'student_enroll_program'
	),

	url(
		regex = r'^my-programs/list/$',
		view = views.StudentProgramListView.as_view(),
		name = 'student_programs'
	),

	url(
		regex = r'^my-programs/(?P<slug>[-\w]+)/detail/$',
		view = views.StudentProgramDetailView.as_view(),
		name = 'student_program_details'
	),

	url(
		regex = r'^my-programs/(?P<slug>[-\w]+)/(?P<pk>[\w-]+)/detail/$',
		view = views.StudentLectureDetailView.as_view(),
		name = 'student_program_course_detail'
	),

	url(
		regex = r'^my-programs/(?P<slug>[-\w]+)/course/(?P<pk>[\w-]+)/module/(?P<module_id>[\w-]+)/contents/$',
		view = views.StudentLectureDetailView.as_view(),
		name = 'student_program_course_module_detail'
	),	
	
	url(
		regex = r'^lecture/list/$',
		view = views.LectureByOwnerListView.as_view(),
		name='lecture-list-by-owner'
	),
	url(
		regex = r'^lecture/(?P<slug>[-\w]+)/module/list/$',
		view = views.ModuleListView.as_view(),
		name='module-list-by-course'
	),
	
	# ----------------------------------------------------------------------------------

	url(
		regex = r'(?P<slug>[-\w]+)/lecture/(?P<lecture_id>[-\w]+)/create/$',
		view = views.LectureModuleUpdateView.as_view(),
		name = 'module_create'
	),
	url(
		regex = r'(?P<slug>[-\w]+)/module/(?P<module_id>\d+)/$',
		view = views.ModuleContentListView.as_view(),
		name = 'module_content_list'
	),
	url(
		regex = r'(?P<slug>[-\w]+)/module/(?P<module_id>\d+)/content/(?P<model_name>\w+)/create/$',
		view = views.ContentCreateUpdateView.as_view(),
		name = 'module_content_create'
	),
	url(
		regex = r'(?P<slug>[-\w]+)/module/(?P<module_id>\d+)/content/(?P<model_name>\w+)/(?P<id>\d+)/edit/$',
		view = views.ContentCreateUpdateView.as_view(),
		name = 'module_content_update'
	),




	# ===========================================================

	url(
		regex = r'^masters/list/$',
		view = views.MasterListView.as_view(),
		name='masters-list'
	),
	url(
		regex = r'^master/(?P<slug>[-\w]+)/details/$',
		view = views.MasterDetailView.as_view(),
		name='detail-master'
	),
	url(
		regex = r'^master/(?P<slug>[-\w]+)/detail/semester/create/$',
		view = views.SemesterMasterCreateView.as_view(),
		name='semester-master-create'
	),
	url(
		regex = r'^master/create/$',
		view = views.MasterCreateView.as_view(),
		name='master-add'
	),
	url(
		regex = r'^master/(?P<pk>\d+)/update/$',
		view = views.MasterUpdateView.as_view(),
		name='master-update'
	),
	
	url(
		regex = r'^bachelors/list/$',
		view = views.BachelorFrontListView.as_view(),
		name='bachelor-front-list'
	),

	url(
		regex = r'^masters/list$',
		view = views.MasterFrontListView.as_view(),
		name='masters-front-list'
	),
	url(
		regex = r'^(?P<slug>[-\w]+)/program/download/$',
		view = views.download,
		name='program-download'
	),
	

]
