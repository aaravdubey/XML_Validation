from lxml import etree

def validate_xml(xml_file, xsd_file):
    try:
        xml_doc = etree.parse(xml_file)
        
        schema_doc = etree.parse(xsd_file)
        
        schema = etree.XMLSchema(schema_doc)
        
        is_valid = schema.validate(xml_doc)
        
        if is_valid:
            print("XML document is valid.")
        else:
            print("XML document is not valid.")
            print("Validation errors:")
            for error in schema.error_log:
                print(f"Line {error.line}, Column {error.column}: {error.message}")
                
    except etree.XMLSyntaxError as e:
        print("Error parsing XML document:", e)

if __name__ == "__main__":
    xml_file = "employees.xml"  
    xsd_file = "employee_schema.xsd"  
    
    validate_xml(xml_file, xsd_file)
