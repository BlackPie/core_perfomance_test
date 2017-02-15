import xlwt

from project.apps.users.models import User
from project.apps.users.templatetags.user_tags import bizzfuzz, is_allowed


def generate_xls():
    user_list = User.objects.all()
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('users')
    first_iteration = True
    line = 1

    for user in user_list:
        column = 0

        for name, value in user.get_fields():
            worksheet.write(line, column, value)

            if first_iteration:
                worksheet.write(line-1, column, name)

            column += 1

        worksheet.write(line, column, is_allowed(user))
        worksheet.write(line, column+1, bizzfuzz(user))
        line += 1

        if first_iteration:
            first_iteration = False

    return workbook
