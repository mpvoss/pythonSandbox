from html import HTML
import InterestUtil


def export(user1, user2, score, runtime):

    h = HTML()
    insertSources(h)

    h.text("<div class=\"container\">",escape=False)
    h.h1('Matched profile analytics', align='center')
    h.p('Common interests: ' + str(score))
    h.p('Runtime: ' + str(runtime))
    t = h.table(klass='table table-bordered table-hover table-striped')
    t.text('<thead>',escape=False)
    r = t.tr
    r.th('Name')
    r.th(user1.name)
    r.th(user2.name)

    t.text('</thead>',escape=False)

    common, unique1, unique2 = InterestUtil.compareInterests(user1.interests, user2.interests)

    for interest in common:
        r = t.tr(klass="success")
        r.td(interest.name)
        r.td(interest.value)
        r.td(interest.value)

    for interest in unique1:
        r = t.tr(klass="")
        r.td(interest.name)
        r.td(interest.value)
        r.td('-')

    for interest in unique2:
        r = t.tr(klass="")
        r.td(interest.name)
        r.td('-')
        r.td(interest.value)


    h.text("</div>",escape=False)

    file = open('output.html', 'w')
    file.write(str(h))

def insertSources(h):
    h.link(rel='stylesheet', href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css')
    h.text("</link>",escape=False)
    h.script(src='https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js')
    h.text("</script>", escape=False)
    h.script(src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js')
    h.text("</script>",escape=False)



def getVal(list, val):
    if len(list) > val:
        return list[val].name + ": " + list[val].value
    else:
        return ""
