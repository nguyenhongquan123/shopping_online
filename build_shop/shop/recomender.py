import redis
from django.conf import settings
from .models import Product

# connect to redis
r = redis.Redis(host=settings.REDIS_HOST,
                        port=settings.REDIS_PORT,
                        db=0,
                        decode_responses=True)

class Recommender(object):
    def get_product_key(self, id):
        return 'product:{}:purchased_with'.format(id)
    
    def products_bought(self, products):
        product_ids = [p.Product_id for p in products]
        for product_id in product_ids:
            for with_id in product_ids:
            # get the other products bought with each product
                if product_id != with_id:
                # increment score for product purchased together
                    r.zincrby(self.get_product_key(product_id),1,with_id)
        r.save()   
    
    def suggest_products_for(self, product_id, max_results=3):
        # only 1 product
        suggestions = r.zrange(self.get_product_key(product_id),
                                        0, -1, desc=True)[:max_results]
        if suggestions==[]:
            suggestions=None
        return suggestions
        

                           
    
    