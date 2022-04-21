from django.contrib.contenttypes.fields import GenericRelation

class GenericRelation_OneToOne(GenericRelation):
    many_to_many = False
    many_to_one = False
    one_to_many = False
    one_to_one = True
    def __init__(self, to, object_id_field='object_id', content_type_field='content_type',
                 for_concrete_model=True, related_query_name=None, limit_choices_to=None, **kwargs):
        
    