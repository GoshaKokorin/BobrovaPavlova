from django.core.mail import EmailMessage

from bp.settings import EMAIL_HOST_USER


def send_contact_mail(data):
    subject = 'Заявка'
    message = f'Имя: {data["name"]}\n' \
              f'Телефон: {data["phone"]}\n'
    from_email = EMAIL_HOST_USER
    recipient_list = EMAIL_HOST_USER

    mail = EmailMessage(subject=subject, body=message, from_email=from_email, to=[recipient_list])
    result = mail.send()
    return result


def send_partners_mail(data):
    subject = 'Заявка от поставщика'
    message = f'Имя: {data["name"]}\n' \
              f'Телефон: {data["phone"]}\n' \
              f'Email: {data["email"]}\n' \
              f'Ссылка: {data["url"]}\n'
    from_email = EMAIL_HOST_USER
    recipient_list = EMAIL_HOST_USER

    mail = EmailMessage(subject=subject, body=message, from_email=from_email, to=[recipient_list])
    result = mail.send()
    return result


def send_vacancies_mail(data):
    subject = 'Заявка по вакансии'
    message = f'Имя: {data["name"]}\n' \
              f'Телефон: {data["phone"]}\n' \
              f'Email: {data["email"]}\n' \
              f'Ссылка: {data["url"]}\n'
    from_email = EMAIL_HOST_USER
    recipient_list = EMAIL_HOST_USER

    mail = EmailMessage(subject=subject, body=message, from_email=from_email, to=[recipient_list])
    result = mail.send()
    return result
