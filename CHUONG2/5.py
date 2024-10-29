import xml.dom.minidom
def main():
    doc = xml.dom.minidom.parse("3.xml")
    print("Company Name:", doc.getElementsByTagName("name")[0].firstChild.nodeValue)
    print(f"{len(doc.getElementsByTagName('name')) - 1} staff member(s):")
    for name in doc.getElementsByTagName("name")[1:]:
        print(name.firstChild.nodeValue)
if __name__ == "__main__":
    main()

   
