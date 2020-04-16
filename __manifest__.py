{
  'name': 'Serial Number',
  'author': 'Bayu Dwi Saputra & Ibnu Nur Khawarizmi',
  'version': '0.1',
  'depends': [
    'sale','product','mrp','mrp_production_draft', 'stock_mts_mto_rule' , 'serial_pabrik'
  ],
  'data': [
    
    'views/mrp_serial_number.xml',
    'report/report_mrp_serial_number.xml', 
    # 'data/mrp_serial_number_sequence.xml'
    
  ],

  'qweb': [

  ],
  'sequence': 4,
  'auto_install': False,
  'installable': True,
  'application': True,
  'category': 'Serial Number',
  'summary': 'Add Product With Serial Number at Sale Order',
  'license': 'OPL-1',
  'images': ['static/description/icon.png'],
  'description': '-'
}
