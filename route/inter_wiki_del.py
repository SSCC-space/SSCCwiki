from .tool.func import *

def inter_wiki_del(conn, tool, name):
    curs = conn.cursor()

    if admin_check(None, tool) == 1:
        if tool == 'del_inter_wiki':
            curs.execute(db_change("delete from html_filter where html = ? and kind = 'inter_wiki'"), [name])
        elif tool == 'del_edit_filter':
            curs.execute(db_change("delete from html_filter where html = ? and kind = 'regex_filter'"), [name])
        elif tool == 'del_name_filter':
            curs.execute(db_change("delete from html_filter where html = ? and kind = 'name'"), [name])
        elif tool == 'del_file_filter':
            curs.execute(db_change("delete from html_filter where html = ? and kind = 'file'"), [name])
        elif tool == 'del_email_filter':
            curs.execute(db_change("delete from html_filter where html = ? and kind = 'email'"), [name])
        elif tool == 'del_image_license':
            curs.execute(db_change("delete from html_filter where html = ? and kind = 'image_license'"), [name])
        elif tool == 'del_extension_filter':
            curs.execute(db_change("delete from html_filter where html = ? and kind = 'extension'"), [name])
        else:
            curs.execute(db_change("delete from html_filter where html = ? and kind = 'edit_top'"), [name])

        conn.commit()

        return redirect('/' + re.sub(r'^del_', '', tool))
    else:
        return re_error('/error/3')