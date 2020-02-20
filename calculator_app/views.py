from django.shortcuts import render
import os
from django.http import HttpResponse
from scripts.interest_parameter_checker import *
from scripts.compound_interest import compound_interest
# Create your views here.




def index(request):
	#return HttpResponse('welcome to home page')
	return render(request, 'calculator_app/index.html')



def interest_calc(request):


	return render(request, 'calculator_app/interest.html')





def results_interest(request):
	error_text = False


	try:
		amount = request.POST['amount']
		interest_rate = request.POST['interest_rate']
		num_times_interest = request.POST['num_times_interest']
		time_period = request.POST['time_period']
		time_periods = request.POST['time_periods']



	except:
		error_text = 'Sorry, no input received. '
		
		return render(request, 'calculator_app/results_interest.html', {
			"error_text" : error_text, "dict" : request.POST, 

			})


	is_valid = interest_parameter_checker(amount, interest_rate, num_times_interest, time_period, time_periods)

	if is_valid:
		compound_interest_ = compound_interest(amount, interest_rate, num_times_interest, time_period, time_periods)

	else:
		compound_interest_ = None

	context_dict = {
		"amount" : amount, 
		"interest_rate" : interest_rate, 	
		"num_times_interest" : num_times_interest, 
		"time_period" : time_period, 
		"time_periods" : time_periods,
		"is_valid" : is_valid, 
		"compound_interest" : compound_interest_


		


	}



	return render(request, 'calculator_app/results_interest.html', context_dict)

	


def loan_calculator(request):

	return render(request, 'calculator_app/loan.html')
