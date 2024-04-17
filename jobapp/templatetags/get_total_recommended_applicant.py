from django import template
register = template.Library()


@register.simple_tag(name='get_total_recommended_applicant')
def get_total_recommended_applicant(total_recommended_applicants , job):

    return total_recommended_applicants[job.id]
  
     



        

