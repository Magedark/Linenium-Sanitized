from behave import *
from icecream import ic

@given(u'a loaded dashboard')
def step_impl(context):
    context.dash.getDashboard(context.url)

@then(u'the correct number of pages are calculated')
def step_impl(context):
    pages = context.dash.pageNavigation()
    assert len(pages) > 0	

@given(u'comics are on the page')
def step_impl(context):
    context.comicsOnPage = context.dash.countComicsOnPage()

@then(u'the number of comics should be greater than 0')
def step_impl(context):
    assert len(context.comicsOnPage) > 0

@given(u'the latest comic number')
def step_impl(context):
	context.latestComicNumber = context.dash.getLatestComicNumber()
	assert context.latestComicNumber > 0

@then(u'the latest comic number should equal total the number of comics')
def step_impl(context):
	context.dash.resetDashboard()
	context.allComics = context.dash.countUpAllComics()
	assert (len(context.allComics) == context.latestComicNumber)