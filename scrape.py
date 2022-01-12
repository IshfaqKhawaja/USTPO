from requests_html import HTMLSession


def find(text, element):
    try:
        index = text.index(element)
        return text[index+1]
    except:
        return ''


def scrape(irnis):
    session = HTMLSession()
    data = {}
    status_url = f'https://tsdr.uspto.gov/statusview/sn{irnis}'
    docs_url = f'https://tsdr.uspto.gov/docsview/sn{irnis}'
    # FETCHING STATUS RELEATED DETAILS
    html = session.get(status_url)
    html = html.html
    text = html.text.split('\n')
    # Finding Mark
    data['Mark'] = find(text, 'Mark:')
    # Finding US Serial Number:
    data['US Serial Number'] = find(text, 'US Serial Number:')
    # Finding Application Filing Date
    data['Application Filing Date'] = find(text, 'Application Filing Date:')
    data['Mark Type'] = find(text, 'Mark Type:')
    data['TM5 Common Status Descriptor'] = find(
        text, 'TM5 Common Status Descriptor:')
    data['TM5 Common Status Descriptor'] += '.' + \
        find(text, data['TM5 Common Status Descriptor'])
    data['Status Date'] = find(text, 'Status Date:')
    data['Publication Date'] = find(text, 'Publication Date:')
    data['Date Abandoned'] = find(text, 'Date Abandoned:')
    try:
        temp = text.copy()
        temp.reverse()
        # Getting Last Occurance
        index = temp.index('International Class(es):')
        data['International Class(es)'] = temp[index-1]
    except:
        data['International Class(es)'] = ''
    data['Owner Name'] = find(text, 'Owner Name:')
    data['Legal Entity Type'] = find(text, 'Legal Entity Type:')

    # Correspodent Name and Address:
    try:
        try:
            index2 = text.index('Phone:')
        except:
            index2 = text.index('Domestic Representative - Not Found')
        finally:
            index2 = -1
        try:
            index1 = text.index('Correspondent Name/Address:')
            if index2 == -1:
                data['Correspondent Name/Address'] = ' '.join(
                    text[index1+1:index1+4])
            else:
                data['Correspondent Name/Address'] = ' '.join(
                    text[index1+1:index2])
        except:
            data['Correspondent Name/Address'] = ''
    except:
        data['Correspondent Name/Address'] = ''
    data['Phone'] = find(text, 'Phone:')
    data['Correspondent e-mail'] = find(text, 'Correspondent e-mail:')

    # END OF FETCHING STATUS RELATED DETAILS:

    # FETCHING DOCUMENTS RELATED DETAILS
    html = session.get(docs_url)
    html = html.html
    links = html.links
    text = html.text.split('\n')
    try:
        index = text.index('Document Type')
        data['Document Date'] = text[index+2]
        data['Document Title'] = text[index+3]

    except:
        data['Document Date'] = ''
        data['Document Title'] = ''

    try:
        index = text.index('Offc Action Outgoing')
        data['Offc Action Date'] = text[index-1]
        docId = text[index+2]
        url = f'https://tsdrsec.uspto.gov/ts/cd/casedoc/sn{irnis}/OOA{docId}/1/webcontent?scale=1'
        html = session.get(url)
        html = html.html
        text = html.text.split('\n')
        index1 = -1
        for i in text:
            if i.find('SUMMARY OF ISSUES') != -1:
                index1 = text.index(i)
                break
        index2 = index1+4
        if index1 != -1:
            for i in text[index1+1:]:
                if i.isupper():  # If Following is Capital String:
                    index2 = text.index(i)
                    break

            data['SUMMARY OF ISSUES'] = '\n'.join(text[index1+1: index2])
        else:
            data['SUMMARY OF ISSUES'] = ''

    except:
        data['SUMMARY OF ISSUES'] = ''
    return data


if __name__ == '__main__':
    print(scrape('79306207'))
