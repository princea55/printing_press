{
    'name': 'printingpress',
    'summary': "This project primarily aimed to develop an Online Production and Sales Management System for a book printing press maangement.",
    'version': '1.0',
    'author': 'TechUltra Solutions',
    'website': 'www.techultrasolutions.com',
    'depends': ['base','crm'],
    'data': [
        #security
        'security/printingpress_security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        

        #view
        'views/printingpress_customer_views.xml',
        'views/printingpress_product_views.xml',
        'views/printingpress_productbook_views.xml',
        'views/printingpress_employees_views.xml',
        'views/printingpress_rowmaterial_views.xml',
        'views/printingpress_suplier_views.xml',
        'views/printingpress_order_views.xml',
        'views/printingpress_vendor_views.xml',
        'views/printingpress_printingbook_views.xml',
        'views/printingpress_productcategory_views.xml',
        'views/printingpress_productsubcategory_views.xml',
        'views/printingpress_language_views.xml',
        'views/printingpress_orderline_views.xml',
        'views/printingpress_employeetype_views.xml',
        'views/printingpress_crm_views.xml',
        'views/printingpress_timemembership_views.xml',
        'views/printingpress_permanentlymembership_views.xml',

        # wizard
        'wizard/printingpress_employeesalary_views.xml',

        #reports
        'views/report_card.xml',
        'views/report_order.xml',


        
        
    ],
    'css': ['static/src/css/common.css'],
    'application':True,
    'auto_install': False,
}
