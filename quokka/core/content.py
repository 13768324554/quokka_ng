# coding: utf-8

from quokka.db import collection_index
from quokka.admin.views import ModelView
from quokka.admin.forms import fields, Form
from flask_admin.model.fields import InlineFieldList  # , InlineFormField
from flask_admin.form import Select2Widget, Select2TagsWidget
# from flask_admin.helpers import get_form_data
from wtforms import validators


# TODO: encapsulate all fields under quokka.admin.fields
# from wtforms_components.fields import SelectField


class ContentForm(Form):
    """Base form for all contents"""

    title = fields.StringField('Title', [validators.required()])
    summary = fields.TextAreaField('Summary')
    category = fields.StringField('Category')
    tags = fields.StringField(
        'Tags',
        widget=Select2TagsWidget(),
        # choices=lambda: []
    )
    slug = fields.StringField('Slug')

    # authors = fields.StringField('authors')
    # authors = fields.FieldList(
    #    fields.StringField('authors', [validators.required()]))

    authors = InlineFieldList(fields.StringField('Authors'))

    date = fields.DateTimeField('Date')
    modified = fields.HiddenField('Modified')

    lang = fields.StringField('Language')
    translations = fields.HiddenField('Translations')
    status = fields.HiddenField('status')

    # metadata
    content_type = fields.SelectField(
        'Type',
        widget=Select2Widget()
    )


class ContentView(ModelView):
    """Base form for all contents"""
    form = ContentForm
    column_list = (
        'title',
        'category',
        'authors',
        'date',
        'modified',
        'lang',
        'status'
    )

    def create_form(self):
        form = super(ContentView, self).create_form()
        form.content_type.choices = [('a', 'a'), ('b', 'b')]
        return form

    def edit_form(self, obj):
        form = super(ContentView, self).edit_form(obj)
        form.content_type.choices = [('a', 'a'), ('b', 'b')]
        return form

    # def edit_form(self, obj):
    #     return Form(get_form_data(), **obj)


def configure(app, db, admin):
    admin.register(
        collection_index,
        ContentView,
        name='Content'
    )
    return 'content'
