from django import forms 
from .models import Products, Category

class ProductForm(forms.ModelForm):
    
    class Meta:
        model : ProductForm
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in cetegories]
        
        self.field['cetegory'].choice = friendly_names
        for field_name, field in self.fields.items():
            field.weiget.attrs['class'] = 'border-black rounded-0'