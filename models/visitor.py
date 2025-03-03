from odoo import models, fields, api
import requests

class IPVisitorTracking(models.Model):

    _name = 'ip.visitor.tracking'
    _description = 'Seguimiento de Visitantes IP'
    _rec_name = 'ip_address'
    
    api_key = fields.Char(string='Clave API', required=True, help='Tu clave API de ipgeolocation.io')
    ip_address = fields.Char(string='IP del Visitante', readonly=True)
    country = fields.Char(string='País', readonly=True)
    city = fields.Char(string='Ciudad', readonly=True)
    latitude = fields.Float(string='Latitud', readonly=True)
    longitude = fields.Float(string='Longitud', readonly=True)
    isp = fields.Char(string='Proveedor de Servicios', readonly=True)
    organization = fields.Char(string='Organización', readonly=True)
    visit_time = fields.Datetime(string='Hora de la Visita', default=fields.Datetime.now, readonly=True)
    
    def get_visitor_location(self):

        api_url = "https://api.ipgeolocation.io/ipgeo?apiKey=" + self.api_key
        
        try:
            response = requests.get(api_url, timeout=3)
            
            if response.status_code != 200:
                error_message = "Error al obtener datos de geolocalización. Código: " + str(response.status_code)
                return {'error': error_message}
            
            data = response.json()
            vals = {
                'ip_address': data.get('ip'),
                'country': data.get('country_name'),
                'city': data.get('city'),
                'longitude': float(data.get('longitude') or 0),
                'latitude': float(data.get('latitude') or 0),
                'isp': data.get('isp'),
                'organization': data.get('organization'),
                'visit_time': fields.Datetime.now()
            }
            self.write(vals)
                
        except Exception as e:
            error_message = "Error de conexión con la API: " + str(e)
            return {'error': error_message}