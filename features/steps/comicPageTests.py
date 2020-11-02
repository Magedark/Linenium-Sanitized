from behave import *
from icecream import ic


@given(u"an uncommented loaded page")
def step_impl(context):
	context.cp.getComic(context.noCommentURL)

@given(u"a page has no comments")
def step_impl(context):
	page = context.cp.commentCounting()
	context.numberOfComments = page["Number of comments"]

@then(u"number of comments should be 0")
def step_impl(context):
	assert context.numberOfComments == 0

@given(u'a loaded page')
def step_impl(context):
	context.cp.getComic(context.commentsURL)

# Divorce the counting of the comments from the clicking of the reply buttons
@then(u'we should look for comments')
def step_impl(context):
	page = context.cp.commentCounting()
	context.currentPage = page
	context.numberOfComments = page["Number of comments"]

@then(u'number of comments should be greater than 0')
def step_impl(context):
	assert context.numberOfComments > 0

@given(u'a comic and a returned page')
def step_impl(context):
	context.currentPage = context.cp.commentCounting()
	assert context.currentPage is not None

@then(u'the name shouldn\'t be blank')
def step_impl(context):
	assert context.currentPage["Name"] is not ""

@then(u'the number of comments should be 0 or more')
def step_impl(context):
    assert context.currentPage["Number of comments"] is not ""

@then(u"the url shouldn't be blank")
def step_impl(context):
    assert context.currentPage["URL"] is not ""
