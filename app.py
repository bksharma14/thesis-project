import os
from flask import Flask
from flask import render_template
from flask import request, redirect
# from pymongo import MongoClient
from fpdf import FPDF
import webbrowser
from values import L1,L2,L3,L4,L5,R1,R2,R3,R4,R5
import matplotlib.pyplot as plt
import numpy as np
from flask import make_response


 

label = ['L1','L2','L3','L4','L5','R1','R2','R3','R4','R5']

# client = MongoClient('localhost:27017')
# db = client.FormData

app = Flask(__name__, static_url_path='/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# PEOPLE_FOLDER = os.path.join('static')
# app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/')
def hello_world():
    return render_template('login.html')

database =  {
  "shivam": "shimmy",
  "bksharma": "thesis"
}

@app.route('/login', methods = ['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    if(username in database):
        if(password == database[username]):
            return render_template('fp.html')
        else:
            return render_template('nologin.html')
    else:
        return render_template('nologin.html')            



    # return render_template('fp.html')

@app.route('/back', methods = ['POST'])
def back():
	return render_template('fp.html')

@app.route('/backtologin', methods = ['POST'])
def backtologin():
    return render_template('login.html')    

@app.route('/signup', methods = ['POST'])
def signup():
    # email = request.form['email']
    # email_addresses.append(email)
    pdf = FPDF(unit='in')
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200*0.0393701, 10*0.0393701, txt="Report", ln=1, align="C")
    pdf.image("fp.png", x = None, y = None, w = 0, h = 0, type = '', link = 'fp.png')
    pdf.set_auto_page_break

    name = request.form['name']
    father = request.form['father']
    dob = request.form['dob']
    address = request.form['address']
    phone = request.form['phone']
    counsellor = request.form['counsellor']

    l1rc = int(request.form['l1rc'])
    l2rc = int(request.form['l2rc'])
    l3rc = int(request.form['l3rc'])
    l4rc = int(request.form['l4rc'])
    l5rc = int(request.form['l5rc'])
    r1rc = int(request.form['r1rc'])
    r2rc = int(request.form['r2rc'])
    r3rc = int(request.form['r3rc'])
    r4rc = int(request.form['r4rc'])
    r5rc = int(request.form['r5rc'])

    l1p = request.form['l1p']
    l2p = request.form['l2p']
    l3p = request.form['l3p']
    l4p = request.form['l4p']
    l5p = request.form['l5p']
    r1p = request.form['r1p']
    r2p = request.form['r2p']
    r3p = request.form['r3p']
    r4p = request.form['r4p']
    r5p = request.form['r5p']

    L1_value = l1rc*L1[l1p]
    L2_value = l2rc*L2[l2p]
    L3_value = l3rc*L3[l3p]
    L4_value = l4rc*L4[l4p]
    L5_value = l5rc*L5[l5p]
    R1_value = r1rc*R1[r1p]
    R2_value = r2rc*R2[r2p]
    R3_value = r3rc*R1[r3p]
    R4_value = r4rc*R4[r4p]
    R5_value = r5rc*R5[r5p]

    sum = L1_value+L2_value+L3_value+L4_value+L5_value+R1_value+R2_value+R3_value+R4_value+R5_value
    sum2 = L1_value+L2_value*0.5+L3_value*0.5+L4_value+L5_value*0.5+R1_value+R2_value+R3_value*0.5+R4_value+R5_value

    percentages = []
    percentages.append(L1_value/sum)
    percentages.append(L2_value/sum)
    percentages.append(L3_value/sum)
    percentages.append(L4_value/sum)
    percentages.append(L5_value/sum)
    percentages.append(R1_value/sum)
    percentages.append(R2_value/sum)
    percentages.append(R3_value/sum)
    percentages.append(R4_value/sum)
    percentages.append(R5_value/sum)

    percentages2 = []
    percentages2.append(L1_value/sum2)
    percentages2.append((L2_value+L5_value)*0.5/sum2)
    percentages2.append((L3_value+R3_value)*0.5/sum2)
    percentages2.append(L4_value/sum2)
    percentages2.append(R5_value/sum2)
    percentages2.append(R2_value/sum2)
    percentages2.append(R4_value/sum2)
    percentages2.append(R5_value/sum2)

    percentages3=[]

    percentages3.append(percentages2[4]+percentages2[5])
    percentages3.append(percentages2[0]+percentages2[4])
    percentages3.append(percentages2[0]+percentages2[1])
    percentages3.append(percentages2[2]+percentages2[7])
    
    percentages4=[]
    percentages4.append(percentages[0]+percentages[5])
    percentages4.append(percentages[1]+percentages[6])
    percentages4.append(percentages[2]+percentages[7])
    percentages4.append(percentages[3]+percentages[8])
    percentages4.append(percentages[4]+percentages[9])


    right_brain = (percentages[0]+percentages[1]+percentages[2]+percentages[3]+percentages[4])*100.0
    left_brain = 100.0 - right_brain 

    fig = plt.figure(figsize=(7, 7))
    index = np.arange(len(label))
    plt.bar(index, percentages)
    plt.xlabel('Fingerprint input', fontsize=15)
    plt.ylabel('Percentage', fontsize=15)
    plt.xticks(index, label, fontsize=15, rotation=30)
    plt.title('Innate Multiple Intelligencies for '+name,fontsize=20)
    plt.plot(range(1)) #plot exampl
    plt.savefig(name+'.png',dpi=fig.dpi)

    for x in percentages:
    	print (x)
    	# y=y+x

    # print(y)	



    # print(phone)

    # db.mydb.insert_one(
    #     {
    #         # "ID": db.form.count() + 1,
    #         "name": name,
    #         "father's name": father,
    #         "date of birth": dob,
    #         "address": address,
    #         "phone": phone,
    #         "counsellor": counsellor
    #         # "isActive": True
    #         # "date": date,
    #         # "time": time
    #     }
    #     )
    pdf.add_page()
    pdf.set_font('Times','B',16)
    pdf.cell(200*0.0393701,40*0.0393701,txt="PERSONAL REPORT",border=1,ln=1,align="C",fill=False)  
    pdf.ln(25*0.0393701)
    pdf.set_font('Times','B',14)
    pdf.cell(200*0.0393701,20*0.0393701,txt="Personal Details",border=0,ln=1,align="C",fill=False)
    #pdf.line(10, 1, 200, 1)
    pdf.set_font('Arial', size=12)
    #pdf.set_xy(50,100)
    pdf.cell(200*0.0393701, 10*0.0393701, txt="Name : "+name, ln=1, align="L")    
    pdf.cell(200*0.0393701, 10*0.0393701, txt="Father's name : " +father, ln=1,align="L") #why no father?
    #pdf.cell(30.0)
    #pdf.image("intelligences.jpg", x = None, y = None, w = 20, h = 20, type = '', link = 'intelligences.jpg')
    #pdf.ln(25)
    pdf.cell(200*0.0393701, 10*0.0393701, txt="Date of birth : " +dob, ln=1, align="L")
    pdf.cell(200*0.0393701, 10*0.0393701, txt="Address : "+ address, ln=1, align="L")
    pdf.cell(200*0.0393701, 10*0.0393701, txt="Phone : "+ phone, ln=1, align="L")
    pdf.set_font('Times','B',14)
    pdf.cell(200*0.0393701,20*0.0393701,txt="Councellor's Details",border=0,ln=1,align="C",fill=False)
    #pdf.line(10, 1, 200, 1)
    pdf.set_font('Arial', size=12) 
    pdf.cell(200*0.0393701, 10*0.0393701, txt="Counsellor's name : "+ counsellor, ln=1, align="L")
    pdf.cell(200*0.0393701, 10*0.0393701, txt="Company Name : ", ln=1, align="L")
    pdf.cell(200*0.0393701, 10*0.0393701, txt="Address : ", ln=1, align="L")
    pdf.cell(200*0.0393701, 10*0.0393701, txt="Contact Number"+ counsellor, ln=1, align="L")

    pdf.add_page()

    nm = name+'.png'
    pdf.image(nm, x = None, y = None, w = 100*0.0393701, h = 100*0.0393701, type = '', link = nm)


    pdf.cell(200*0.0393701,10*0.0393701, txt="your intrapersonal percentage score is " + str(percentages[0]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="your logical ability percentage score is " + str(percentages[1]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="your fine motor skills percentage score is " + str(percentages[2]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="your language ability percentage score is " + str(percentages[3]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="your nature love percentage score is " + str(percentages[4]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="your interpersonal percentage score is " + str(percentages[5]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="your visualization percentage score is " + str(percentages[6]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="your gross motor skills percentage score is " + str(percentages[7]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="your music, sound percentage score is " + str(percentages[8]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="your visual appreciation percentage score is " + str(percentages[9]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="your Right Brain percentage score is " + str(right_brain),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="your Left Brain percentage score is " + str(left_brain),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="your visual learning style score is" +str())
    
    #pdf.image("brain_organization.jpg", x = None, y = None, w = 100*0.0393701, h = 100*0.0393701, type = '', link = 'brain_organization.jpg')
    #pdf.image("brain_lobes.jpg", x = None, y = None, w = 10, h = 10, type = '', link = 'brain_lobes.jpg')

    pdf.cell(200*0.0393701,10*0.0393701,txt="HELLO",ln=1,align="C")
    pdf.cell(200*0.0393701,10*0.0393701, txt="according to the 2nd algorithm your interpersonal percentage score is " + str(percentages2[0]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="according to the 2nd algorithm your visual percentage score is " + str(percentages2[1]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="according to the 2nd algorithm your kinesthic percentage score is " + str(percentages2[2]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="according to the 2nd algorithm your musical percentage score is " + str(percentages2[3]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="according to the 2nd algorithm your intrapersonal percentage score is " + str(percentages2[4]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="according to the 2nd algorithm your logical percentage score is " + str(percentages2[5]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="according to the 2nd algorithm your language percentage score is " + str(percentages2[6]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="according to the 2nd algorithm your naturalist percentage score is " + str(percentages2[7]*100),ln=1,align="L")

    pdf.cell(200*0.0393701,10*0.0393701, txt="according to the 2nd algorithm your IQ percentage score is " + str(percentages3[0]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="according to the 2nd algorithm your EQ percentage score is " + str(percentages3[1]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="according to the 2nd algorithm your CQ percentage score is " + str(percentages3[2]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="according to the 2nd algorithm your AQ percentage score is " + str(percentages3[3]*100),ln=1,align="L")

    pdf.cell(200*0.0393701,10*0.0393701, txt="according to the 1st algorithm your ACTION percentage score is " + str(percentages4[0]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="according to the 1st algorithm your THINK percentage score is " + str(percentages4[1]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="according to the 1st algorithm your TACTILE percentage score is " + str(percentages4[2]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="according to the 1st algorithm your AUDITORY percentage score is " + str(percentages4[3]*100),ln=1,align="L")
    pdf.cell(200*0.0393701,10*0.0393701, txt="according to the 1st algorithm your VISUAL percentage score is " + str(percentages4[3]*100),ln=1,align="L")
    
#class PDF(FPDF):
    #def footer(self):
        # Go to 1.5 cm from bottom
        #self.set_y(-1)
        # Select Arial italic 8
        #self.set_font('Arial', 'I', 8)
        # Print centered page number
        #self.cell(1, 1, 'what the fuck', 0, 0, 'C')


#     pdf.add_page()

# # Remember to always put one of these at least once.
#     pdf.set_font('Times','',10)

#     # Long meaningless piece of text
#     loremipsum = """Disclaimer: The information provided in this anaylsis belongs its owner only\
#     , in case of a minor the rights of its information are with\
#     in case of a minor the rights of its information are with his legal guardian. By\
#     agreeing to this analysis you are giving you fingerprints voluntarily and in case of minor you are representing him as legal guardian or parent. \
#     It is also understood that these fingerprints are used only for analyzing and preparing this report and these fingerprints\
#     are not stored with us in any form. The content of this analysis are only for reference basis on the scientific research. The decision to follow any instruction, advise\
#     , suggestion or recommendation completely depends upon you and you will be solely responsible for the consequences of the same. We as an organization or any of its representative is not responsible for any consequences under any circumstance.\
#     Before taking any crucial decision please refer to your family doctor, psychiatrist or psychologist. The results are only indicative and the company or any authorized representative of the company shall in no case be liable for failure in any particular course of study or activity recommended in the report.\

#     """

    effective_page_width = pdf.w - 2*pdf.l_margin



#     pdf.set_font('Times','B',10)
#     pdf.cell(1,0.0, 'Without multi_cell using effective page width:')
#     pdf.ln(0.25)
#     pdf.set_font('Times','',10.0)
#     # Cell is as wide as the effective page width
#     pdf.cell(effective_page_width, 0.0, loremipsum)
#     pdf.ln(0.5)
#     pdf.set_font('Times','B',10.0)
#     pdf.cell(1,0.0, 'Using multi_cell and effective page width:')
#     pdf.ln(0.25*1)

#     pdf.set_font('Times','',10)
#     # Cell is as wide as the effective page width
# # and multi_cell requires declaring the height of the cell.
#     pdf.multi_cell(effective_page_width,1*0.15, loremipsum)
#     pdf.ln(0.5*1)

# Cell half as wide as the effective page width
# and multi_cell requires declaring the height of the cell.
#     pdf.set_font('Times','B',10)
#     pdf.cell(1,0.0, 'Using multi_cell and half the effective page width:')
#     pdf.ln(0.25*1)

#     pdf.set_font('Times','',10)
#     pdf.multi_cell(effective_page_width/2, 1*0.15, loremipsum)
#     pdf.ln(0.5*1)
# #pdf.footer()

    pdf.add_page()
    #pdf.footer()

    pdf.set_font('Times','B',20)
    pdf.cell(effective_page_width,0.50,txt="PERSONAL REPORT",border=1,ln=1,align="C",fill=False)
    pdf.ln(1)
    pdf.set_font('Times','B',14)
    pdf.cell(effective_page_width,0.15,txt="Personal Details",border=0,ln=1,align="C",fill=False)
        #pdf.line(10, 1, 200, 1)
    pdf.set_font('Arial', size=12)
    pdf.ln(1)
        #pdf.set_xy(50,100)
    pdf.cell(effective_page_width, 0.15, txt="Name : ", ln=1, align="L")
    pdf.ln(0.25)
    pdf.cell(effective_page_width, 0.15, txt="Father's name : ", ln=1,align="L")
    pdf.ln(0.25)#why no father?
        #pdf.cell(30.0)
        #pdf.image("intelligences.jpg", x = None, y = None, w = 20, h = 20, type = '', link = 'intelligences.jpg')
        #pdf.ln(25)
    pdf.cell(effective_page_width, 0.15, txt="Date of birth : ", ln=1, align="L")
    pdf.ln(0.25)
    pdf.cell(effective_page_width, 0.15, txt="Address : ", ln=1, align="L")
    pdf.ln(0.25)
    pdf.cell(effective_page_width, 0.15, txt="Phone : ", ln=1, align="L")
    pdf.ln(0.25)
    pdf.set_font('Times','B',14)
    pdf.cell(effective_page_width,0.15,txt="Councellor's Details",border=0,ln=1,align="C",fill=False)
    pdf.ln(1)
    #pdf.line(10, 1, 200, 1)
    pdf.set_font('Arial', size=12)
    pdf.cell(effective_page_width, 0.15, txt="Counsellor's name : ", ln=1, align="L")
    pdf.ln(0.25)
    pdf.cell(effective_page_width, 0.15, txt="Company Name : ", ln=1, align="L")
    pdf.ln(0.25)
    pdf.cell(effective_page_width, 0.15, txt="Address : ", ln=1, align="L")
    pdf.ln(0.25)
    pdf.cell(effective_page_width, 0.15, txt="Contact Number", ln=1, align="L")
    pdf.ln(1.4)

    # pdf.set_font('Arial', size=8)
    # pdf.multi_cell(effective_page_width, 0.15, loremipsum)

    # #pdf.footer()

    pdf.add_page()


    pdf.set_font('Times','B' 'I', 18)
    pdf.cell(effective_page_width,0.15,txt="WELCOME",border=0,ln=1,align="C",fill=False)
    pdf.ln(1)
    pdf.set_font('Arial', size=12)
    pdf.cell(effective_page_width,0.20,txt="Dear NAME",border=0,ln=1,align="L",fill=False)
    pdf.ln(0.35)
    pdf.multi_cell(effective_page_width,0.25,txt="It gives me immense pleasure to Congratulate you for undergoing Dermatoglyphics Multiple Intelligence Test!",align="L",fill=False)
    pdf.ln(0.35)
    pdf.multi_cell(effective_page_width,0.25,txt="You are indeed very fortunate to take part in this Scientific & Revolutionary technology for making best choices in your life.",align="L",fill=False)
    pdf.ln(0.35)
    pdf.multi_cell(effective_page_width,0.25,txt="We love greeting new clients as it allows us the opportunity to describe Family Education India philosophy. There is nothing in this World, or even outside, which an enlightened and empowered brain cannot achieve. Through this Test, we strive to identify your truest innate abilities, the best career options for you and your strongest areas. Our aim is to bring a meaningful transformation and a positive change in your life by unleashing the true and hidden potential of your brain.",align="L",fill=False)
    pdf.ln(0.35)
    pdf.multi_cell(effective_page_width,0.25,txt="By taking this test you have already proven two great things about yourself one, you love yourself and those who love you; and, two, you are desirous of going on a sojourn of self discovery.",align="L",fill=False)
    pdf.ln(0.35)
    pdf.multi_cell(effective_page_width,0.25,txt="Today, my friend, you will find the answers to some of the most fundamental questions concerning you and your life. Each page of this analysis report will unfold your true potential, inborn talent, multiple intelligences, most suitable learning  style  & much  more. Our team  of highly dexterous Psychologists analyses and evaluates various parameters of your innate abilities to arrive upon their inferences about you.",align="L",fill=False)
    pdf.ln(0.35)
    pdf.multi_cell(effective_page_width,0.25,txt="I am sure that this report will work as a lamp post on your pathways to success",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.25,txt="Best Regards",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.25,txt="COUNSELLOR",align="L",fill=False)
    pdf.ln(0.3)

    pdf.add_page()
    pdf.set_font('Times', '', 10.0)

    #Effective page width, or just epw
    epw = pdf.w - 2 * pdf.l_margin

    # Set column width to 1/4 of effective page width to distribute content
    # evenly across table and page
    col_width = epw / 3
    # Since we do not need to draw lines anymore, there is no need to separate
    # headers from data matrix.
    data = [['Sr. No.', 'Contents', 'Page Number'],
            ['1', 'ABOUT DERMATOGLYPHICS', '5'],
            ['2', 'BRAINS LOBES & THEIR FUNCTIONS','6'],
            ['3', 'DOWN SYNDROME',  '7'],
            ['4', 'ATD ANGLE', '8'],
            ['5', 'MY INNATE & MULTIPLE INTELLIGENCES', '10'],
            ['6', 'THEORY OF MULTIPLE INTELLIGENCES', '11'],
            ['7', 'QUOTIENTS', '21'],
            ['8', 'CAREER OPTIONS','22'],
            ['9', 'CAREER GRAPHS',  '26'],
            ['10', 'BRAIN DOMINANCE','27'],
            ['11', 'LEARNING STYLE',  '28'],
            ['12', 'PERSONALITY BEHAVIOUR', '32'],
            ['13', 'DISC PROFILE/EXTRA CURRICULAR', '33'],
            ['14', 'SWOT ANALYSIS',  '35'],
            ['15', 'ACQUIRING METHODS', '36'],
            ['16', 'PREFERRED STREAM','37'],
            ['17', 'SYPNOSIS OF ANALYSIS', '38'],
            ['18', 'TOTAL FINGER RIDGE COUNT', '39'],
            ['19', 'REMARK', '40']
    ]

    # Document title centered, 'B'old, 14 pt
    pdf.set_font('Times', 'B', 18.0)
    pdf.cell(epw, 0.0, 'INDEX', align='C')
    pdf.set_font('Times', '', 10.0)
    pdf.ln(0.5)
    # Text height is the same as current font size
    th = pdf.font_size  # Enter data in colums
            # Notice the use of the function str to coerce any input to the
            # string type. This is needed
            # since pyFPDF expects a string, not a number.
    # Line break equivalent to 4 lines
    pdf.set_font('Arial', '', 9.0)
    pdf.ln(0.5)
    for row in data:
        for datum in row:
            # Enter data in colums
            pdf.cell(col_width, 3 * th, str(datum), border=1)

        pdf.ln(3 * th)
    pdf.cell(effective_page_width,0.2,txt="Dear NAME",align="L",fill=False)
    pdf.ln(0.25)
    pdf.ln(0.25)
    pdf.cell(effective_page_width,0.2,txt="Dear NAME",align="L",fill=False)
    pdf.ln(0.25)


    pdf.add_page()

    pdf.set_font('Times','B',20)
    pdf.cell(effective_page_width,0.50,txt="ABOUT DERMATOGLYPHICS",ln=1,align="C",fill=False)
    pdf.ln(1)
    pdf.set_font('Arial', size=12)
    pdf.multi_cell(effective_page_width,0.25,txt="Dermatoglyphics, derived from ancient greek words derma meaning skin and glyph meaning carving, is the scientific study of the fingerprints.it is a proven scientific method to decode brain's talent through the physical formation of fingerprints, which has linkage to brain development.It is not palmistry and is not future telling.",align="L",fill=False)
    pdf.ln(0.35)
    pdf.multi_cell(effective_page_width,0.25,txt="Dermatoglyphics is a professional industry that combines neurobiology, genetics, brain science and embryology coupled with clinical studies. In developing this system, Dermatoglyphics experts conducted psychological pattern profiles with more than 500 thousand individuals since 1985 across China, Japan, Korea, Taiwan, Singapore and Malaysia to generate a database for cross comparison study which can help individuals to learn the way to discover their inner potential..",align="L",fill=False)
    pdf.ln(0.35)
    pdf.multi_cell(effective_page_width,0.25,txt="Dermatoglyphics Multiple intelligences is scientifically proven. Besides,data acquistion process is computerized & clinically proven. Besides, data acquisition process computerized. Therefore, we can achieve an accuracy of more than 90%. Body prints formation & formation of brain are synchronized with the fetus in the mother's body in the first 13 weeks and first 19 weeks. It has been medically proven that body prints and existence of multiple intelligences are completely linked.",align="L",fill=False)
    pdf.ln(0.35)
    pdf.multi_cell(effective_page_width,0.25,txt="Further in relation to Dermatoglyphics, the multiple intelligences theory by professor Howard Gardner states that multiple intelligences exist in the brain system and further identify the brain structures which are in charge of the intelligence area",align="L",fill=False)
    pdf.ln(0.35)
    pdf.set_font('Times','B',16)
    pdf.cell(effective_page_width,0.50,txt="Some Key References & Researches",ln=1,align="C",fill=False)
    pdf.ln(0.5)
    pdf.set_font('Arial','I', size=12)
    pdf.cell(effective_page_width,0.3,txt="The Hand As a mirror of Systemic Disease by Theodore J. Berry, M.D.F.A.C.P., 1963 Dermatoglyphics",ln=1,align="L",fill=False)
    pdf.cell(effective_page_width,0.3,txt="Frames of Mind by Dr. Howard Gardner, 1998",ln=1,align="L",fill=False)
    pdf.cell(effective_page_width,0.3,txt="Multiple Intelligence by Dr. Howard Gardner, 1996 ",ln=1,align="L",fill=False)
    pdf.cell(effective_page_width,0.3,txt="4th REFERENCE?? ",ln=1,align="L",fill=False)
    pdf.cell(effective_page_width,0.3,txt="5th REFERENCE?? ",ln=1,align="L",fill=False)
    pdf.cell(effective_page_width,0.3,txt="6th REFERENCE??? ",ln=1,align="L",fill=False)

    pdf.add_page()
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Brain Lobes & Functions",ln=1,align="C",fill=False)
    pdf.ln(1)
    pdf.set_font('Arial','B', size=10)
    pdf.multi_cell(effective_page_width,0.25,txt="Brain is divided into 5 parts/lobes & every lobe has pre-defined, specific role to do.",align="C",fill=False)
    pdf.ln(0.2)
    pdf.image("brain.jpg", x=None, y=None, w=5, h=3, type='', link='brain.jpg')
    pdf.ln(0.5)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width,0.25,txt="Further brain is divided in 2 parts, Left Brain and Right Brain. Left brain controls right side of the body & vice- versa.",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.25,txt="Science has proved that within the same lobe, Left & Right brain do different specific roles. So, brain has 10 compartments - 5 Left & 5 right, each compartment is having specific and pre-defined function. Further our brain has approximately 1200 crores Neuron cells, which are divided in random order into these 10 compartments",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.25,txt="One compartment has less neuron count while other has more. It is impossible that two persons have same neuron distribution.",align="L",fill=False)
    pdf.ln(0.3)
    pdf.image("brain2.jpg", x=None, y=None, w=0, h=0, type='', link='brain2.jpg')



    pdf.add_page()
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Down Syndrome Fingerprint",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.image("down1.jpg", x=1, y=None, w=6, h=4, type='', link='down1.jpg')
    pdf.ln(0.7)
    pdf.set_font('Arial', size=14)
    pdf.multi_cell(effective_page_width,0.25,txt="As we mentioned earlier that fingerprints start developing from 13th week's of gestation period and this is the same period when the brain also start developing.",align="L",fill=False)
    pdf.ln(0.5)
    pdf.multi_cell(effective_page_width,0.25,txt="The development of fingerprints and brain happen simultaneously and they have direct co-relation between them. ",align="L",fill=False)
    pdf.ln(0.5)
    pdf.multi_cell(effective_page_width,0.25,txt="Science has proven that the child whose brain is not developed, his fingerprints are also found undeveloped. This disease is called Down Syndrome and this is congenital in nature",align="L",fill=False)
    pdf.ln(0.5)
    pdf.multi_cell(effective_page_width,0.25,txt="Down syndrome patients are 100% mentally retarded and their fingerprints are also undeveloped",align="L",fill=False)
    pdf.ln(0.5)
    pdf.multi_cell(effective_page_width,0.25,txt=" Their ATD angles are also found more than 55 Degrees.",align="L",fill=False)
    pdf.ln(0.5)

    pdf.add_page()
    pdf.ln(0.8)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="ATD Angle & Learning Sensibility",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Arial', size=10)
    pdf.cell(effective_page_width*0.5,0.3,txt="LEFT_NUMBER",ln=0,align="L",fill=False)
    pdf.cell(effective_page_width*0.5,0.3,txt="RIGHT_NUMBER",ln=1,align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.3,txt="The brain is mainly made up of neurons. A nerve cell receives signals from other neurons or sensory organs, processes these signals, and sends signals to other neurons, muscles or bodily organs",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.3,txt="ATD angle reflects degree & speed of co-ordination  between the nervous muscular system. reflecting one's efficiency",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.3,txt="ATD angle is a Dermatoglyphics trait formed by drawing lines between the triadic below the first and last digits and the most proximal tirades on the hyposthenia region of palm.",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.3,txt="Since early 70's Soviet Union had been applying Dermatoglyphics and ATD angle in selecting athletes. In the countries like China, Australia, Japan, Malaysia, Taiwan etc. The selection/rejection of the candidate depends upon the findings of Dermatoglyphics & ATD angle and if the findings are supporting then the coach and other authorities of the sports team focus and concentrate on the training on such students.",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.3,txt="This is one of the key reasons that China has won the maximum no. of Gold medals in Olympics since beginning. Lower the ATD, more the athlete material you are.",align="L",fill=False)
    pdf.ln(0.3)
    pdf.set_font('Times','B',16)
    pdf.cell(effective_page_width*0.5,0.3,txt="ATD Angle <35 Degree :-",ln=1,align="L",fill=False)
    pdf.ln(0.2)
    pdf.set_font('Arial', size=12)
    pdf.multi_cell(effective_page_width,0.3,txt="You are born athlete. You will do very well in your favorite sport. Your eye movement and hand coordination is excellent.",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.3,txt="You have sharp observation skills & agile task performing abilities. You are smart and active in your personal learning & development.",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.3,txt="For really tough things, even a small clue can take you to the target. You are full of energy with excellent fine & gross motor skills.",align="L",fill=False)

    pdf.add_page()
    pdf.set_font('Times','B',16)
    pdf.cell(effective_page_width*0.5,0.3,txt="ATD Angle 35-40 Degrees :-",ln=1,align="L",fill=False)
    pdf.ln(0.2)
    pdf.set_font('Arial', size=12)
    pdf.multi_cell(effective_page_width,0.3,txt="This is within a range of actively smart people. You are good in your personal learning and can take sports as a hobby and can develop it. You are much better than so many other people in task performing ability, observation skills, eye to hand coordination etc. However taking sports as a career will be challenging for you but your physical movements are better than ordinary people & you are a health conscious person.",align="L",fill=False)
    pdf.ln(0.4)
    pdf.set_font('Times','B',16)
    pdf.cell(effective_page_width*0.5,0.3,txt="ATD Angle 41-45 Degrees :-",ln=1,align="L",fill=False)
    pdf.ln(0.2)
    pdf.set_font('Arial', size=12)
    pdf.multi_cell(effective_page_width,0.3,txt="This is within a range of good people. majority of the people fall in this category. You are normal in your personal learning, generally not passionate for sports, playing. If you don't pay attention to your health and weight then chances are that you may put weight over a period of time, specially after the age of 45. You will perform above the crowd in your takes performing ability, observation skills and learning but hard work is required to excel.",align="L",fill=False)
    pdf.ln(0.4)
    pdf.set_font('Times','B',16)
    pdf.cell(effective_page_width*0.5,0.3,txt="ATD Angle 46-50 Degrees :-",ln=1,align="L",fill=False)
    pdf.ln(0.2)
    pdf.set_font('Arial', size=12)
    pdf.multi_cell(effective_page_width,0.3,txt="This is average in performance. The people with ATD in this range need step by step learning methods. They take their own time to perform takes or observe things. We need to repeated things while teaching them. They find it difficult to understand multiple instruction at a time and they avoid fast speech or instructions. Sport is not meant for them, they generally dislike exercise, morning-walk or yoga.",align="L",fill=False)
    pdf.ln(0.4)
    pdf.set_font('Times','B',16)
    pdf.cell(effective_page_width*0.5,0.3,txt="ATD Angle >50 Degrees :-",ln=1,align="L",fill=False)
    pdf.ln(0.2)
    pdf.set_font('Arial', size=12)
    pdf.multi_cell(effective_page_width,0.3,txt="This may be a case of special child/person. The child/person may be partially or fully mentally retorted.",align="L",fill=False)
    pdf.ln(0.4)

    pdf.add_page()
    pdf.ln(0.8)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="My Innate %  Multiple Intelligences",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Arial', size=10)
    pdf.cell(effective_page_width*0.5,0.30,txt="NAME XYZ",ln=0,border=1,align="L",fill=False)
    pdf.cell(effective_page_width*0.5,0.30,txt="ANALYSIS",ln=1,border=1,align="L",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Times','',11.0)
    column_width=1.8
    column_spacing=0.2
    ybefore=pdf.get_y()
    pdf.multi_cell(column_width, 0.2, "INTRAPERSONAL ASPECT: Self achievement & ego planning & executing determines good or bad self understanding")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing, ybefore)
    pdf.multi_cell(column_width, 0.2, "add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+2, ybefore)
    pdf.multi_cell(column_width, 0.2, "add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+4, ybefore)
    pdf.multi_cell(column_width, 0.2, "INTERPERSONAL ASPECT Personality and behaviour Leadership skills  Goal and Vision           Understanding others")
    ybefore1=pdf.get_y()
    pdf.ln(0.4)
    pdf.multi_cell(column_width, 0.2, "LOGICAL THNKING Concepts, Process, Maths, Science,Grammar, Reasoning and analyis")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing,ybefore1)
    pdf.multi_cell(column_width, 0.2, "                                                                         add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+2,ybefore1)
    pdf.multi_cell(column_width, 0.2, "                                                                         add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+4,ybefore1)
    pdf.multi_cell(column_width, 0.2, "                                                               VISUALIZATION   Imagination Idea formation Visual & Spatial abilities 3D recognition")
    ybefore2=pdf.get_y()
    pdf.ln(0.4)
    pdf.multi_cell(column_width, 0.2, "  FINE MOTOR SKILLS Hand control Finger skills action identification writing")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing,ybefore2)
    pdf.multi_cell(column_width, 0.2, "                                                                          add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+2,ybefore2)
    pdf.multi_cell(column_width, 0.2, "                                                                          add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+4,ybefore2)
    pdf.multi_cell(column_width, 0.2, "                                                                                         GROSS MOTOR SKILLS      Sports Activities Outdoor activities     ")
    ybefore3=pdf.get_y()
    pdf.ln(0.4)
    pdf.multi_cell(column_width, 0.2, "LANGUAGE ABILITY Words spoken or written word formation and memory speech and communication")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing,ybefore3)
    pdf.multi_cell(column_width, 0.2, "                                                                          add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+2,ybefore3)
    pdf.multi_cell(column_width, 0.2, "                                                                          add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+4,ybefore3)
    pdf.multi_cell(column_width, 0.2, "                                             MUSIC, SOUND rhythm, tone, listening skills, auditory feel, emotion and feeling")
    ybefore4=pdf.get_y()
    pdf.ln(0.6)
    pdf.multi_cell(column_width, 0.2, "NATURE LOVE Observation, skills, senses-touch taste smell reading Environment centric")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing,ybefore4)
    pdf.multi_cell(column_width, 0.2, "                                                                          add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+2,ybefore4)
    pdf.multi_cell(column_width, 0.2, "                                                                          add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+4,ybefore4)
    pdf.multi_cell(column_width, 0.2, "                                                                                     VISUAL APPRECIATION Maps Visual Interpretation Art & drawing aesthetic sense")
    pdf.ln(1)

    pdf.set_font('Times', '', 10.0)
    epw = pdf.w - 2 * pdf.l_margin

    col_width = epw /5
    data1 = [['ACTION', 'THINK', 'TACTILE','AUDITORY','VISUAL'],
            ['num1', 'num2', 'num3','num4','num5'],
            ]
    pdf.set_font('Times', '', 10.0)
    th1 = pdf.font_size  # Enter data in colums
    pdf.set_font('Arial', '', 9.0)
    for row in data1:
        for datum in row:
            # Enter data in colums
            pdf.cell(col_width, 3 * th1, str(datum), border=1)
        pdf.ln(3 * th)

    pdf.add_page()
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Dr Howard Gardner & Theory of Multiple Intelligence",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width*0.6,0.25,txt="Dr. Howard Gardner, a renowned scientist, psychologist & educationist, is the Hobbs Professor of Cognition and Education at the Harvard Graduate School of Education and Senior Director of Harvard Project Zero. Among numerous honors, Gardner received a MacArthur Prize Fellowship in 1981. He has received honorary degrees from twenty-two colleges and universities",align="L",fill=False)
    pdf.image("howard.jpg", x=effective_page_width*0.3+3, y=2, w=3, h=3, type='', link='howard.jpg')
    pdf.ln(1.5)
    pdf.multi_cell(effective_page_width,0.25,txt="In 2005 he was selected by Foreign Policy and Prospect magazines as one of 100 most influential public intellectuals in the world. The author of over twenty books translated into twenty-seven languages, and several hundred articles, Gardner is best known in educational circles for his Theory of Multiple Intelligences proposed in 1983, which has been widely accepted by science all over the world. And today there are many schools across the world which are running on the education pattern of Theory of Multiple Intelligence. He has also written extensively on creativity, leadership, and professional ethics. His latest book Five Minds for the Future was published in April 2007. Here are the details of 8 multiple intelligences proposed by him.",align="L",fill=False)
    pdf.image("types.jpg", x=None, y=None, w=effective_page_width, h=3.5, type='', link='types.jpg')


    pdf.add_page()
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Intrapersonal Intelligence",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width,0.3,txt="This intelligence has to do with understanding & interacting with self",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.3,txt="People with high Interpersonal Intelligence are usually introvert and usually prefer to work alone. They are highly self aware and capable of understanding their own mood, feelings, temperaments, motivation, strength & weakness.",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.3,txt="They often have an infinity for thoughts based on philosophical approach. They learn the best when allowed to concentrate on the subject themselves. There is often high level of perfection associated with this intelligence.",align="L",fill=False)
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Remedies to develop your intrapersonal intelligence",ln=1,align="C",fill=False)
    pdf.ln(0.4)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width,0.2,txt="1.Learn to meditate or just set aside quiet time alone to think.",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="2.Study philosophy especially the different schools of thought from different cultures",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="3.Find a counselor or therapist and explore yourself.",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="4.Create your own personal ritual that makes you feel good as often as you choose to.",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="5.Record and analyze your dreams.",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="6.Read self-help books and listen to tapes.",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="7.Establish a quiet place in your home for introspection.",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="8.Develop an interest or hobby that sets you apart from the crowd.",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="9.Make a personal development plan.",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="10.Keep a daily journal for recording your thoughts, dreams, goals, feelings and memories.",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="11.Study biographies of great individuals with powerful personalities who made a real impact on the world.",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="12. Keep a daily journal",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="13.Spend time with people who have strong & healthy sense of self.",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="14.Write autobiography.",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="15.Love yourself.",align="L",fill=False)
    pdf.ln(0.1)

    pdf.add_page()
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Interpersonal Intelligence",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width,0.3,txt="This intelligence has to do with understanding & interacting with others",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.3,txt="People with high Interpersonal Intelligence are usually extrovert and are usually characterized by their sensitivity to other's mood, feelings, temperaments, motivation and their ability to cooperate and work as team member.",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.3,txt="They communicate easily and emphasize with others and may be either leader or follower. They typically learn best by working with others and often enjoy discussion and debate",align="L",fill=False)
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Remedies to develop your Interpersonal Intelligence",ln=1,align="C",fill=False)
    pdf.ln(0.4)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width,0.2,txt="1. Get organized! Use a time management system to make sure you keep in touch regularly with your network of business associates and friends.",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="2. Join a volunteer or service-oriented group.",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="3. Start a hobby that involves you having to go to a regular meeting of like-minded people",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="4. Join the Samaritans",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="5. Throw a party for unknown people",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="6. Take a leadership role at work or in the community.",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="7. Start your own support group",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="8. Participate in workshops/seminars of interpersonal & communication skills.",align="L",fill=False)
    pdf.multi_cell(effective_page_width,0.2,txt="9. Have regular family meetings.",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="10. Strike up conversation with people in public places",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="11.Find several pen friends from different cultures and parts of the world",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="12.Offer to tutor other people on an informal basis in something you have expertise in",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="13.Spend fifteen minutes a day just people-watching on a train, bus, shopping centre or restaurant",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="14. Study the lives of well known people and decide what you want to model from them",align="L",fill=False)
    pdf.ln(0.1)



    pdf.add_page()
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Logical Intelligence",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width,0.3,txt="This intelligence has to do with logic,abstract, reasoning & numbers",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.3,txt="People with high Logical Mathematical Intelligence are generally good in mathematics, chess, computer programming, puzzles and other numerical activities.",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.3,txt="People with high Logical Intelligence tend to be good in reasoning capabilities, scientific thinking, complex calculation, investigation and analysis.",align="L",fill=False)
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Remedies to develop your Logical Mathematical Intelligence",ln=1,align="C",fill=False)
    pdf.ln(0.4)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width,0.2,txt="1.Play logical/mathematical games (Go, Clue do) with friends & family",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="2.Earn to use an abacus",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="3. Work on logic puzzles and brain teasers",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="4. Learn basic computer programming",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="5. Take course in basic math's or science at an evening class",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="6. Read the business sections of the newspaper and look up unfamiliar economic or financial concepts",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="7. Visit a science museum",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="8. Tape yourself talking out loud about how to solve logical or mathematical problems",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="9. Help your kids with their math's/science homework",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="10.Purchase a telescope and a microscope and discover a myriad of new world",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="11.Draw flowcharts of all the key processes in your department or area of work and then come up with new ideas on how to make whatever service you provide more effective",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="12.Practice mental calculation.",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="13.Avoid using calculator",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="14.Develop the habit of asking 'Why' ",align="L",fill=False)
    pdf.ln(0.1)


    pdf.add_page()
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Visual Intelligence",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width,0.3,txt="This intelligence has to do with visual & spatial judgement",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.3,txt="People with high Visual Intelligence are usually very good at visualizing and mentally creating and manipulating the objects. They are inclined towards artistic work and have good visual memory",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.3,txt="People with high Visual Intelligence have good sense of directions. They are also good at eye-hand coordination. High Visual Intelligence",align="L",fill=False)
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Remedies to develop your Visual Intelligence",ln=1,align="C",fill=False)
    pdf.ln(0.4)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width,0.2,txt="Draw a picture of a problem or issue",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="Create a mind map of a problem or a issue",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="3. Use diagrams and flowcharts instead of words",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="4. Make visual notes of what someone is saying rather than using words",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="Encourage yourself to doodle whilst thinking",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="6.Use notes to track contents of meeting",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="7. Keep a personal sketchbook within which to draw pictures of your ideas",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="8. Join painting classes",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="9. Participate in drawing competition.",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="10.Work on Jig-saw puzzle, Rubik Cube, Maze or other Visual Puzzles",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="11.Learn photography",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="12.Study geometry",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="13.Learn ideographical based language like Chinese",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="14.Purchase a visual dictionary and study how a common machine works",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="15.Learn how to use flow chart, decision trees, diagrams and other forms of visual representations",align="L",fill=False)
    pdf.ln(0.1)


    pdf.add_page()
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Kinesthetic Intelligence",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width,0.3,txt="This intelligence has to do with body movement and physical activities",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.3,txt="People with high Kinesthetic Intelligence are usually very good at body movement, physical activities, dance, jogging, walking, swimming, sports etc",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.3,txt="People with high Kinesthetic Intelligence are good in building making things. They learn best by doing things rather than listenin reading things. They are good at muscle memory too.",align="L",fill=False)
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Remedies to develop your Kinesthetic Intelligence",ln=1,align="C",fill=False)
    pdf.ln(0.4)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width,0.2,txt="1.Learn to juggle",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="2.Join a sports team",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="3. Put on a blindfold and have a friend lead you around to explore the environment with your hands",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="4. Take lessons in golf, swimming, tennis or gymnastics",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="5.Learn a martial art like aikido, judo or karate.",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="6.Exercise regularly and keep track of the idea that occur to you during sessions",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="7.Learn a craft such as woodworking,sewing, weaving or pottery",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="8. Build models",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="9. Walk on the curb, balance beams or low walls to improve your sense of balance",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="10.Learn how to give a great massage",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="11.Help children with arts and crafts",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="12.Develop hand-eye co-ordination by bowling, tossing or basketballs",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="13.Take a class in acting or join a local amateur dramatic company",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="14.Play video games that require the use of quick reflexes",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="15.Take formal lessons in dance (modern, ballroom, etc.).",align="L",fill=False)
    pdf.ln(0.1)

    pdf.add_page()
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Linguistic Intelligence",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width,0.3,txt="This intelligence has to do with words,spoken or written",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.3,txt="People with high Linguistic Intelligence have good command over their words, language and are expressive in nature. They are typic good at reading, writing, telling stories and memorizing dates and words",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.3,txt="People with high Linguistic Intelligence tend to learn through readi taking notes, listening lectures. They are good in discussion and debate. They are good at explaining to others, teaching and delive speeches",align="L",fill=False)
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Remedies to develop your Linguistic Intelligence",ln=1,align="C",fill=False)
    pdf.ln(0.4)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width,0.2,txt="1. Play word games (e.g. scrabble, anagrams, crosswords, up words)",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="2. Join a book club",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="3. Attend a workshop on writing through a local college",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="4. Record yourself speaking and listen to the playback.",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="5. Visit the library and bookshops regularly",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="6. Join a speech improvement club",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="7. Subscribe to a high-quality newspaper",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="8. Read a new book every month",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="9. Prepare an informal ten-minute talk for a business or community event",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="10. Learn to use a word processor",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="11.Listen and watch recordings of famous orators",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="12. Write in your daily diary or write 250 words a day about anything on your mind",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="13. Find opportunities to tell stories to children and adults",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="14. Make up your own riddles, puns and jokes",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="15.Attend a speed-reading seminar",align="L",fill=False)
    pdf.ln(0.1)


    pdf.add_page()
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Musical Intelligence",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width,0.3,txt="This intelligence has to do with rhythm,sound & music",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.3,txt="People with high Musical Intelligence display great sensitivity towards sound, rhythm, tone and music. They usually have good pitch and are able to sing or play musical instruments and compose music. They respond well towards rhythmic pattern and can be easily distracted by sound",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.3,txt="There is a strong oral component in this intelligence, so those are good in this intelligence, can learn easily through a lecture mode. They may tune-in to music while studying or doing some other work",align="L",fill=False)
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Remedies to develop your Musical Intelligence",ln=1,align="C",fill=False)
    pdf.ln(0.4)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width,0.2,txt="1. Sing in the shower",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="2. Play name the tune game",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="3. Go to concerts or musicals",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="4. Listen to your musical collection regularly",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="5. Join a choir",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="6. Regularly read poetry",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="7. Learn to play a musical instrument",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="8. Spend one hour a week listening to an unfamiliar style of music for you (e.g. jazz, country & western, classical, folk, heavy rock, house music, etc.)",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="9. Buy an electronic keyboard and learn simple melodies and chords.",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="10. Put on background music whilst studying,cooking,dressing or eating",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="11. Listen for naturally occurring melodies such as footsteps, birdsong even washing machines",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="12. Learn to identify birds by their song",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="13. Create a musical autobiography by collecting recordings of music that has been important to you at different times of your life",align="L",fill=False)
    pdf.ln(0.1)


    pdf.add_page()
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Naturalist Intelligence",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width,0.3,txt="This intelligence has to do with understanding the natural world",align="L",fill=False)
    pdf.ln(0.3)
    pdf.multi_cell(effective_page_width,0.3,txt="People with high Naturalist Intelligence are generally good in observation. They are environment centric and have great love for nature. They love greenery, river, mountains, beaches etc",align="L",fill=False)
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Remedies to develop your Naturalist Intelligence",ln=1,align="C",fill=False)
    pdf.ln(0.4)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width,0.2,txt="1. Create observation notebooks",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="2. Describe changes in the local or global environment that affect you",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="3. Become involved in the care for pets, wildlife, gardens, or parks",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="4. Use binoculars, telescopes, microscopes, or magnifiers to see things differently",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="5. Photograph natural objects",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="6. Create mind maps to explore, categorize and develop your thinking about problems and issues",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="7. Use all the senses while studying",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="8. Watching animal behavior (squirrels or birds in the schoolyard",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="9. Use a microscope, telescope, binoculars or hand lens",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="10. Keep track of the outdoors over the course of the school year",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="11. Watching the weather ",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="12. Notice ecological principles in action (e.g. decomposition of plant or animal material over time)",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="13. Keep a nature journal",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="14.Imitating a biologist or ecologist doing field studies",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="15.Listing data about characteristics (size, color, form, function, etc",align="L",fill=False)
    pdf.ln(0.1)
    pdf.multi_cell(effective_page_width,0.2,txt="16.Keeping data in a log, blog or diary",align="L",fill=False)
    pdf.ln(0.1)

    pdf.add_page()
    pdf.ln(4)
    pdf.image("types2.jpg", x=None, y=None, w=effective_page_width, h=2.8, type='', link='types2.jpg')

    pdf.add_page()
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="My Quotients",ln=1,align="C",fill=False)
    pdf.ln(0.3)
    pdf.image("QT.jpg", x=None, y=None, w=effective_page_width, h=3.5, type='', link='QT.jpg')

    #pdf.add_page()
    #pdf.ln(0.3)
    #pdf.set_font('Times', '', 10.0)
    #epw = pdf.w - 2 * pdf.l_margin

    #col_width3 = epw /4
    #data3 = [['Music', 'star1', 'Music,Sound,Choreography','Music Teacher Sound Engineering Music Director Instrument Engineering Music Composer'],
            #['Agricultural', 'star2', 'Agronomy, Gardening, Forestry, Agro Specialist, Fishery, Natural Resource Management','Agricultural Engineer Agronomy Researcher Forest Officer Zoo Operator Gardner Nursery Owner'],
            #['Designing', 'num2', 'Contractor, Construction, Engineering, Interior Design, Fashion  Design, Map Design','Civil Engineer Contractor Surveyor Interior Designer Fashion Designer Architect Property Planner/Developer'],
            #['Engineering', 'num2', 'Electronics, Electricals, Computer, Mechanical, Production','Automobile Engineer Chemical Engineer Electrical Engineer Electronics Engineer Mechanical Engineer Computer Engineer'],
            #['Medical Science', 'num2', 'Medical, Pharmacy, Public Hygiene, Food Nutrition, Medical Practitioner, Sports Nutrition, Medical Management','Doctor Pharmacist Nutritionist Drug Officer Medical Editor Surgeon'],
            #]
    #pdf.set_font('Times', '', 10.0)
    #th1 = pdf.font_size  # Enter data in colums
    #pdf.set_font('Arial', '', 9.0)
    #for row in data3:
      #  for datum in row:
     #       # Enter data in colums
       #     pdf.multi_cell(col_width, 8 * th1, str(datum), border=1)
        #pdf.ln(3 * th)
    pdf.add_page()
    pdf.ln(0.8)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="My Innate % Multiple Intelligences",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Arial', size=10)
    pdf.cell(effective_page_width*0.5,0.30,txt="NAME XYZ",ln=0,border=1,align="L",fill=False)
    pdf.cell(effective_page_width*0.5,0.30,txt="ANALYSIS",ln=1,border=1,align="L",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Times','',11.0)
    column_width=1.8
    column_spacing=0.2
    ybefore=pdf.get_y()
    pdf.multi_cell(column_width, 0.2, "Music")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing, ybefore)
    pdf.multi_cell(column_width, 0.2, "add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+2, ybefore)
    pdf.multi_cell(column_width, 0.2, "Music,Sound,Choreography")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+4, ybefore)
    pdf.multi_cell(column_width, 0.2, "Music Teacher Sound Engineering Music Director Instrument Engineering Music Composer")
    ybefore1=pdf.get_y()
    pdf.ln(0.4)
    pdf.multi_cell(column_width, 0.2, "Agricultural Science")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing,ybefore1)
    pdf.multi_cell(column_width, 0.2, "                                                                      add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+2,ybefore1)
    pdf.multi_cell(column_width, 0.2, "                                                                      Agronomy, Gardening, Forestry, Agro Specialist, Fishery, Natural Resource Management")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+4,ybefore1)
    pdf.multi_cell(column_width, 0.2, "                                                               Agricultural Engineer Agronomy Researcher Forest Officer Zoo Operator Gardner Nursery Owner")
    ybefore2=pdf.get_y()
    pdf.ln(0.4)
    pdf.multi_cell(column_width, 0.2, "  Designing")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing,ybefore2)
    pdf.multi_cell(column_width, 0.2, "                                                                          add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+2,ybefore2)
    pdf.multi_cell(column_width, 0.2, "                                                                          Contractor, Construction, Engineering, Interior Design, Fashion  Design, Map Design")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+4,ybefore2)
    pdf.multi_cell(column_width, 0.2, "                                                                                         Civil Engineer Contractor Surveyor Interior Designer Fashion Designer Architect Property Planner/Developer")
    ybefore3=pdf.get_y()
    pdf.ln(0.4)
    pdf.multi_cell(column_width, 0.2, "Engineering")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing,ybefore3)
    pdf.multi_cell(column_width, 0.2, "                                                                          add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+2,ybefore3)
    pdf.multi_cell(column_width, 0.2, "                                                           Electronics, Electricals, Computer, Mechanical, Production")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+4,ybefore3)
    pdf.multi_cell(column_width, 0.2, "                                                           MUSIC, SOUND rhythm, tone, listening skills, auditory feel, emotion and feeling")
    ybefore4=pdf.get_y()
    pdf.ln(0.6)
    pdf.multi_cell(column_width, 0.2, "Medical")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing,ybefore4)
    pdf.multi_cell(column_width, 0.2, "                                                                          add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+2,ybefore4)
    pdf.multi_cell(column_width, 0.2, "                                                                          Electronics, Electricals, Computer, Mechanical, Production")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+4,ybefore4)
    pdf.multi_cell(column_width, 0.2, "                                                                                     Automobile Engineer Chemical Engineer Electrical Engineer Electronics Engineer Mechanical Engineer Computer Engineer")
    pdf.ln(1)

    pdf.add_page()
    pdf.ln(0.8)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="My Innate % Multiple Intelligences",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Arial', size=10)
    pdf.cell(effective_page_width*0.5,0.30,txt="NAME XYZ",ln=0,border=1,align="L",fill=False)
    pdf.cell(effective_page_width*0.5,0.30,txt="ANALYSIS",ln=1,border=1,align="L",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Times','',11.0)
    column_width=1.8
    column_spacing=0.2
    ybefore=pdf.get_y()
    pdf.multi_cell(column_width, 0.2, "Literature")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing, ybefore)
    pdf.multi_cell(column_width, 0.2, "add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+2, ybefore)
    pdf.multi_cell(column_width, 0.2, "Hindi, English, History, Political Science")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+4, ybefore)
    pdf.multi_cell(column_width, 0.2, "Hindi Teacher English Teacher History Teacher Political Science Teacher Author Poet")
    ybefore1=pdf.get_y()
    pdf.ln(0.4)
    pdf.multi_cell(column_width, 0.2, "Mathematics & Analyst")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing,ybefore1)
    pdf.multi_cell(column_width, 0.2, "                                                                      add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+2,ybefore1)
    pdf.multi_cell(column_width, 0.2, "                                                                      Mathematics, Chemistry, Physics, Accounts, Economics")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+4,ybefore1)
    pdf.multi_cell(column_width, 0.2, "                                                               Mathematician Physicist Chemist Business Analyst Accountant Finance Officer Actuary")
    ybefore2=pdf.get_y()
    pdf.ln(0.4)
    pdf.multi_cell(column_width, 0.2, "  Management")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing,ybefore2)
    pdf.multi_cell(column_width, 0.2, "                                                                          add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+2,ybefore2)
    pdf.multi_cell(column_width, 0.2, "                                                                          Business Management, Information Management, Marketing Management, Hotel Management, Recreation Management")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+4,ybefore2)
    pdf.multi_cell(column_width, 0.2, "                                                                           Business Manager Marketing Manager HR Manager Production Manager Tourism Manager Sales Manager")
    ybefore3=pdf.get_y()
    pdf.ln(0.4)
    pdf.multi_cell(column_width, 0.2, "Public & Political Affairs")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing,ybefore3)
    pdf.multi_cell(column_width, 0.2, "                                                                          add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+2,ybefore3)
    pdf.multi_cell(column_width, 0.2, "                                                          Public Relations, Law, Politics, Revolutionary ")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+4,ybefore3)
    pdf.multi_cell(column_width, 0.2, "                                                          Politician MLA Lawyer Judge Public Relationship Officer IAS/IPS Officer Teacher/Professor")
    ybefore4=pdf.get_y()
    pdf.ln(0.6)




    pdf.add_page()
    pdf.ln(0.8)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="My Innate % Multiple Intelligences",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Arial', size=10)
    pdf.cell(effective_page_width*0.5,0.30,txt="NAME XYZ",ln=0,border=1,align="L",fill=False)
    pdf.cell(effective_page_width*0.5,0.30,txt="ANALYSIS",ln=1,border=1,align="L",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Times','',11.0)
    column_width=1.8
    column_spacing=0.2
    ybefore=pdf.get_y()
    pdf.multi_cell(column_width, 0.2, "Psychology")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing, ybefore)
    pdf.multi_cell(column_width, 0.2, "add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+2, ybefore)
    pdf.multi_cell(column_width, 0.2, "Counselor, Practitioner, Psychologist")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+4, ybefore)
    pdf.multi_cell(column_width, 0.2, "Counselor Career Guide Psychologist Mediator Researcher Parenting Specialist")
    ybefore1=pdf.get_y()
    pdf.ln(0.4)
    pdf.multi_cell(column_width, 0.2, "Foreign Languages")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing,ybefore1)
    pdf.multi_cell(column_width, 0.2, "                                                                      add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+2,ybefore1)
    pdf.multi_cell(column_width, 0.2, "                                                                      Languages & Linguistic Education")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+4,ybefore1)
    pdf.multi_cell(column_width, 0.2, "                                                               English Teacher Foreign Language Teacher News Reader Translator Linguistic Researcher Foreign Trader Foreign Affair Personnel")
    ybefore2=pdf.get_y()
    pdf.ln(0.4)
    pdf.multi_cell(column_width, 0.2, "  Sports")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing,ybefore2)
    pdf.multi_cell(column_width, 0.2, "                                                                          add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+2,ybefore2)
    pdf.multi_cell(column_width, 0.2, "                                                                          Sports Industry, Bollywood Industry, TV & Media ")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+4,ybefore2)
    pdf.multi_cell(column_width, 0.2, "                                                                          Cricketer Footballer Swimmer Tennis Player Gym Owner Carom Player Snooker Player")
    ybefore3=pdf.get_y()
    pdf.ln(0.4)
    pdf.multi_cell(column_width, 0.2, "Defense")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing,ybefore3)
    pdf.multi_cell(column_width, 0.2, "                                                                          add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+2,ybefore3)
    pdf.multi_cell(column_width, 0.2, "                                                          Defense Services")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+4,ybefore3)
    pdf.multi_cell(column_width, 0.2, "                                                          Army Air Force Police CRPF Navy Fire Brigade Officer")
    ybefore4=pdf.get_y()
    pdf.ln(0.6)



    pdf.add_page()
    pdf.ln(0.8)

    pdf.add_page()
    pdf.ln(0.8)
    pdf.image("leftright.jpg", x=None, y=None, w=effective_page_width, h=4.5, type='', link='leftright.jpg')
    data5 = [['LEFT BRAIN', 'leftsidenumber', 'RIGHT BRAIN','rightsidenumb']
            ]
    pdf.set_font('Times', '', 10.0)
    th1 = pdf.font_size  # Enter data in colums
    col_width5 = epw / 4
    pdf.set_font('Arial', '', 9.0)
    for row in data5:
        for datum in row:
            # Enter data in colums
            pdf.cell(col_width5, 3 * th1, str(datum), border=1,align="C")
        pdf.ln(3 * th)
    pdf.ln(0.5)
    pdf.multi_cell(effective_page_width,0.25,txt="Left Brain Dominance : Analytical brain, more inclined towards self aware, logical thinking, fine motor skills based activities, language & grammar and may have a hidden love towards nature. They people are generally good in academics. They have convergent thinking and can bring their energy and focus at one point. They prefer to respond to verbal instructions. They like to solve the problems by looking at the parts of things. They are able  locate the differences in similar things easily. They are more planned and structured. Prefer multiple choices tests. They have the ability to control their feelings and emotions. They like Building blocks, puzzles, word forming, problem solving, crosswords etc",align="L",fill=False)
    pdf.ln(0.5)
    pdf.multi_cell(effective_page_width,0.25,txt="Right Brain Dominance : Creative brain, more inclined towards interpersonal skills, imagination, gross motor skills activities, music, colors, pictures, dance, art, rhythms, acting, painting, modeling, fashion, outdoor sports etc. They are generally good in extra curricular activities, primarily creative ones. They tend to throw the rules out of window. They have divergent thinking which is full of creativity and ideas. And they are often lost in their own ideas,  thoughts and world. They may be physically present, mentally absent. Right brain people prefer to respond to demonstrated instruction. They like to solve the problems by looking at the problem as a whole. They are able draw the whole picture in their mind easily. They are more intuitive and work upon feelings. Their emotions and feelings have no limits, and they generally come out",align="L",fill=False)


    pdf.add_page()
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="My Learning Style",ln=1,align="C",fill=False)
    pdf.ln(0.4)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width*0.6,0.25,txt="                                                                                                                                                                                                                                                                                                                                                                                              num1                                                                    Prefer to use graphics, pictures, graphs etc to learn",align="L",fill=False)
    pdf.image("visual.jpg", x=effective_page_width*0.3+3, y=1, w=2.5, h=2, type='', link='visual.jpg')
    pdf.ln(2)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width*0.6,0.25,txt="                                                                                                                                                                                                                                                                                                                                                                                              num2                                                                    Prefer to use listening & discussion to learn",align="L",fill=False)
    pdf.image("audit.jpg", x=effective_page_width*0.3+3, y=4, w=2.5, h=2, type='', link='audit.jpg')
    pdf.ln(2)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width*0.6,0.25,txt="                                                                                                                                                                                                                                                                                                                                                                                              num3                                                                    Prefer to use physical hands and practical activities to learn",align="L",fill=False)
    pdf.image("kin.jpg", x=effective_page_width*0.3+3, y=8, w=2.5, h=2, type='', link='kin.jpg')

    pdf.add_page()
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Visual Learner",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Visual Learning percentage is NUM1",align="L",fill=False)
    pdf.ln(0.2)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Visual Learner learn best by seeing",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They like to read silently",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They enjoy visual simulation,color,vivid imagery",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Relate most effectively to written information",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They can remember faces but forget names",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They notice visual effects in movies",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They enjoy watching TV, movies, etc",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They like to study alone and quietly",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They folllow instructions and directions",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They are good at reading and spellings",align="L",fill=False)
    pdf.image("visual.jpg", x=effective_page_width*0.3+3, y=2, w=2.5, h=2, type='', link='visual.jpg')
    pdf.ln(1)
    pdf.set_font('Times','B',18)
    pdf.cell(effective_page_width*0.5,0.25,txt="Study Tips",align="L",border=1,fill=False)
    pdf.ln(0.3)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Use imagination power to remember facts and lines",align="L",fill=False)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Provide written instructions and ask them to read carefully",align="L",fill=False)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Avoid group discussions, they prefer one to one study",align="L",fill=False)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Watching audio visual for study purpose",align="L",fill=False)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Make outline of everything you study",align="L",fill=False)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Copy what's written on the board",align="L",fill=False)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Convert the linear text or passage in the form of diagram & then study",align="L",fill=False)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Make web notes rather than linear notes.",align="L",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Times','B',18)
    pdf.cell(effective_page_width*0.5,0.25,txt="Best Test Type",align="L",ln=1,border=1,fill=False)
    pdf.set_font('Arial', size=10)
    pdf.ln(0.3)
    pdf.cell(effective_page_width*0.5,0.25,txt="Diagramming,reading maps,esays(if you've studied using an outline),showing a process note etc.",align="L",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Times','B',18)
    pdf.cell(effective_page_width*0.5,0.25,txt="Worst Test Type",align="L",ln=1,border=1,fill=False)
    pdf.set_font('Arial', size=10)
    pdf.ln(0.3)
    pdf.cell(effective_page_width*0.5,0.25,txt="Oral test, listen & respond test etc",align="L",fill=False)

    pdf.add_page()
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt=" Auditory Learner",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt=" Auditory Learning percentage is NUM1",align="L",fill=False)
    pdf.ln(0.2)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Auditory learners learn best by listening",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They like to read out loud",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They are not afraid to speak in class",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They like oral reports",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They are good at explaining things",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They can remember names easily",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They notice sound effects in movies",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They enjoy music. They read slowly",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They can't kee quiet for long",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They are good at grammar and foreign language",align="L",fill=False)

    pdf.image("audit.jpg", x=effective_page_width*0.3+3, y=2, w=2.5, h=2, type='', link='audit.jpg')
    pdf.ln(0.5)
    pdf.set_font('Times','B',18)
    pdf.cell(effective_page_width*0.5,0.25,txt="Study Tips",align="L",border=1,fill=False)
    pdf.ln(0.3)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Use word association",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Provide oral along with written instructions",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Include whole group discussions",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Watching audio-visual which compliment the written test",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Repeat facts with eyes closed",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They take longer time to read passage, so give them sufficient time to read",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="If possible, record the study material, and listen to it frequently",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Allow them to listen to music while studying, specially math's or science",align="L",fill=False)

    pdf.ln(0.3)
    pdf.set_font('Times','B',18)
    pdf.cell(effective_page_width*0.5,0.25,txt="Best Test Type",align="L",ln=1,border=1,fill=False)
    pdf.set_font('Arial', size=10)
    pdf.ln(0.3)
    pdf.cell(effective_page_width*0.5,0.25,txt="Auditory Learners are good at writing responses to lectures they've heard. They're also good at oral tests",align="L",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Times','B',18)
    pdf.cell(effective_page_width*0.5,0.25,txt="Worst Test Type",align="L",ln=1,border=1,fill=False)
    pdf.set_font('Arial', size=10)
    pdf.ln(0.3)
    pdf.cell(effective_page_width*0.5,0.25,txt="Reading passage and writing answers about them in a timed test",align="L",fill=False)

    pdf.add_page()
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt=" Kinesthetic Learner",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt=" Kinesthetic Learning percentage is NUM1",align="L",fill=False)
    pdf.ln(0.2)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Kinesthetic learners learn best by doing",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They like to read along with walking or moving",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Respond while practically doing things rather than listening/reading",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They are good at sports/outdoor activities",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They are generally not good at spelling",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They notice action & body moves in movies.",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They enjoy dancing while listening to to music",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They tap a pencil while studying",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="They like adventure books",align="L",fill=False)
    pdf.image("kin.jpg", x=effective_page_width*0.3+3, y=2, w=2.5, h=2, type='', link='kin.jpg')
    pdf.ln(0.2)
    pdf.set_font('Times','B',18)
    pdf.cell(effective_page_width*0.5,0.25,txt="Study Tips",align="L",border=1,fill=False)
    pdf.ln(0.3)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Use practical/doing approach to teach them",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Teach them through different activities",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Use role plays while teaching them",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Use flash cards to memorize",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Allow them to walk while studying",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Ask them to hold the book in their hands while reading",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Sit near the door or someplace else, where they can easily get up and move around",align="L",fill=False)
    pdf.multi_cell(effective_page_width*0.5,0.25,txt="Illustrate your ideas by drawing maps,diagrams,graphs & tables",align="L",fill=False)
    pdf.ln(0.3)
    pdf.set_font('Times','B',18)
    pdf.cell(effective_page_width*0.5,0.25,txt="Best Test Types",align="L",ln=1,border=1,fill=False)
    pdf.set_font('Arial', size=10)
    pdf.ln(0.3)
    pdf.cell(effective_page_width*0.5,0.25,txt="Short definitions, fill-ins, multiple choice or participate in practical exam rather than written or viva",align="L",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Times','B',18)
    pdf.cell(effective_page_width*0.5,0.25,txt="Worst Test Type",align="L",ln=1,border=1,fill=False)
    pdf.set_font('Arial', size=10)
    pdf.ln(0.3)
    pdf.cell(effective_page_width*0.5,0.25,txt="Long tests, essays, written test, written description etc",align="L",fill=False)


    pdf.add_page()
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Personality & Behaviour",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width*0.6,0.25,txt="Dr. William Moulton Morston was a psychologist and an anthropologer who after studying thousands the human behaviors and their personalities, developed the concept of DISC profile. After his many years of research he submitted his thesis in late 1920's which divides the human personalities into 4 categories i.e. Dominant, Influential, Steady & Compliant.  DISC profile has been in use for many years for multiple purposes like sales, marketing, management, HR, alliances etc. Later on another scientist,  Dr. Gary Couture added bird profiling to the same theory",align="L",fill=False)
    pdf.ln(0.2)
    pdf.image("doctor.jpg", x=effective_page_width*0.7, y=1.6, w=2.5, h=2.5, type='', link='doctor.jpg')
    pdf.ln(1)
    pdf.image("disc.jpg", x=1.5, y=5.5, w=5, h=4, type='', link='disc.jpg')
    #pdf.multi_cell(effective_page_width,0.25,txt="In 2005 he was selected by Foreign Policy and Prospect magazines as one of 100 most influential public intellectuals in the world. The author of over twenty books translated into twenty-seven languages, and several hundred articles, Gardner is best known in educational circles for his Theory of Multiple Intelligences proposed in 1983, which has been widely accepted by science all over the world. And today there are many schools across the world which are running on the education pattern of Theory of Multiple Intelligence. He has also written extensively on creativity, leadership, and professional ethics. His latest book Five Minds for the Future was published in April 2007. Here are the details of 8 multiple intelligences proposed by him.",align="L",fill=False)
    #pdf.image("types.jpg", x=None, y=None, w=effective_page_width, h=3.5, type='', link='types.jpg')

    pdf.add_page()
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="DISC PROFILE",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.image("doctor2.jpg", x=effective_page_width*0.35, y=1.6, w=2.5, h=2.5, type='', link='doctor2.jpg')
    pdf.ln(3)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width,0.25,txt="William Moulton Marston also known by the pen name Charles Moulton, was an American psychologist, inventor and comic book writer who created the character Wonder Woman",align="L",fill=False)
    pdf.ln(0.4)
    pdf.multi_cell(effective_page_width,0.25,txt="Dr. William Moulton Marston was a psychologist and an anthropologer who after studying thousands of human behaviors and their personalities, developed the concept of DISC profile in 1928",align="L",fill=False)
    pdf.ln(0.4)
    pdf.multi_cell(effective_page_width,0.25,txt="After his many years of research he submitted his thesis in late 1920's which divides the human personalities into 4 categories i.e. D for Dominant, I for Influential, S for Steady and C for Compliant (or DISC for short). DISC profile has been in use for many years for multiple purposes like sales, marketing, management, HR, alliances etc",align="L",fill=False)
    pdf.ln(0.4)
    pdf.multi_cell(effective_page_width,0.25,txt="Over the years, different versions of the same theory developed including BEST (Bold, Expressive, Sympathetic, Technical). Later on another scientist, Dr. Gary Couture added bird profiling to  the same theory - Eagle, Peacock, Dove and Owl and it became very popular worldwide",align="L",fill=False)

    pdf.add_page()
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Personality & Behaviour - DISC Profile",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.image("personality.jpg", x=1.5, y=2, w=6, h=7, type='', link='personality.jpg')

    pdf.add_page()
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="SWOT Analysis",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.image("swot1.jpg", x=1.5, y=2, w=5.5, h=3.5, type='', link='swot1.jpg')
    pdf.image("swot2.jpg", x=1.5, y=5.5, w=5.5, h=3.5, type='', link='swot2.jpg')

    pdf.add_page()
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="My Acquiring Methods",ln=1,align="C",fill=False)
    pdf.ln(1.6)
    pdf.set_font('Arial', size=10)
    column_width=1.8
    column_spacing=0.2
    ybefore=pdf.get_y()
    pdf.multi_cell(column_width, 0.2, "Self-Cognitive (Learn by self-inspiration. You are goal oriented & self demanding)")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing, ybefore)
    pdf.multi_cell(column_width, 0.2, "     add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+2, ybefore)
    pdf.multi_cell(column_width, 0.2, "*    Independent                 *   Goal Oriented               *   Target Centric                      *   Self-Starter                          * Stubborn                          * Confident                         * Inflexible                          *   Controller")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+4, ybefore)
    pdf.multi_cell(column_width, 0.2, "*Bold                           *Determined              *Aggressive                     *In charge                         *Rigid                                  *Self-Centric                         *Bossy                             *Bullish")
    ybefore1=pdf.get_y()
    pdf.ln(0.4)
    pdf.multi_cell(column_width, 0.2, "Affective (Learns by imitations/copying)")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing,ybefore1)
    pdf.multi_cell(column_width, 0.2, "                                                                             add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+2,ybefore1)
    pdf.multi_cell(column_width, 0.2, "                                                                                         *   Imitation Learner                *High Learnability  *  Stretchable                       * Flexible                                  * People Oriented                  *  Need Motivation               * Team Player")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+4,ybefore1)
    pdf.multi_cell(column_width, 0.2, "                                                                                     *Cooperative                    *May lack of confidence *Relationship Oriented *Patient                       *Supportive                          *Sensitive ")
    ybefore2=pdf.get_y()
    pdf.ln(0.8)
    pdf.multi_cell(column_width, 0.2, "Reverse Thinker (You have an unique personal style)")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing,ybefore2)
    pdf.multi_cell(column_width, 0.2, "                                                                                                                                                                                               add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+2,ybefore2)
    pdf.multi_cell(column_width, 0.2, "                                                                                        *Reverse Thinker   * Thinking out of the box *   Creative                  * Doing something new       * Doing something different * Dislike traditional style of  working")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+4,ybefore2)
    pdf.multi_cell(column_width, 0.2, "                                                                          *Discoverer                        *Dislike following world      *Rule breaker                       *Milestone                             *Setter                                  *Scientific Thinking               *Impatient                     *Curious")
    ybefore3=pdf.get_y()
    pdf.ln(0.8)
    pdf.multi_cell(column_width, 0.2, "Reflective (You learn better when there is someone to lead, teach & remind you)")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing,ybefore3)
    pdf.multi_cell(column_width, 0.2, "                                                                                                                                                                                           add_number")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+2,ybefore3)
    pdf.multi_cell(column_width, 0.2, "                                                                                         *   Unlimited potential  *  Highly flexible  *Conservative                    * May be talkative      * People oriented                 * Friendly                  *   Defensive")
    pdf.set_xy(column_width + pdf.l_margin + column_spacing+4,ybefore3)
    pdf.multi_cell(column_width, 0.2, "                                                                                         *Limited risk taker             *Lack of Time Management *Lack of discipline        *Need support to perform the best *Need a guide")
    ybefore4=pdf.get_y()
    pdf.ln(0.8)

    pdf.add_page()
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Your Preffered Stream",ln=1,align="C",fill=False)
    pdf.ln(1.6)
    pdf.set_font('Arial','B',16)
    pdf.multi_cell(effective_page_width,0.30,txt="Stream Selection",align="C")
    #GRAPH HERE
    pdf.set_font('Arial', size=10)
    pdf.ln(3.6)
    pdf.multi_cell(effective_page_width,0.20,txt="Stream selection recommendation for studies post high school is based upon outcome of Multiple Intelligence on various in-born attributes identified. Individual if pursue recommended stream is expected to out-perform with lesser of efforts and best of performance and learning resulting in expectional execution and outcome",align="C")

    pdf.add_page()
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="This is me",ln=1,align="C",fill=False)
    pdf.ln(0.6)
    pdf.set_font('Arial', size=12)
    pdf.cell(effective_page_width,0.50,txt="My Innate abilities,quantified, are as follows:- ",ln=1,align="L",fill=False)
    pdf.set_font('Arial', size=10)
    col_width = epw /4
    data6 = [['Intrapersonal', 'Logical', 'Linguistic','Naturalist'],
            ['num1', 'num2', 'num3','num4'],
            ]
    pdf.set_font('Times', '', 10.0)
    th1 = pdf.font_size  # Enter data in colums
    pdf.set_font('Arial', '', 9.0)
    for row in data6:
        for datum in row:
            # Enter data in colums
            pdf.cell(col_width, 3 * th1, str(datum), border=1)
        pdf.ln(3 * th)
    col_width = epw / 4
    data7 = [['Interpersonal', 'Visual', 'Kinesthetic', 'Musical'],
             ['num1', 'num2', 'num3', 'num4'],
             ]
    pdf.set_font('Times', '', 10.0)
    th1 = pdf.font_size  # Enter data in colums
    pdf.set_font('Arial', '', 9.0)
    for row in data7:
        for datum in row:
            # Enter data in colums
            pdf.cell(col_width, 3 * th1, str(datum), border=1)
        pdf.ln(3 * th)
    pdf.ln(0.4)
    pdf.cell(effective_page_width,0.50,txt="Your personality type is that of a XYZ",ln=1,align="L",fill=False)
    pdf.ln(0.4)
    pdf.cell(effective_page_width,0.50,txt="Your brain dominance is divided into-:",ln=1,align="L",fill=False)
    pdf.ln(0.2)
    pdf.cell(effective_page_width*0.5,0.3,txt="LEFT_brain",ln=0,align="C",fill=False)
    pdf.cell(effective_page_width*0.5,0.3,txt="RIGHT_brain",ln=1,align="C",fill=False)
    pdf.ln(0.4)
    pdf.cell(effective_page_width,0.50,txt="Your Learning Styles is divided into",ln=1,align="L",fill=False)
    pdf.ln(0.2)
    pdf.cell(effective_page_width*0.33,0.3,txt="VISUAL XYZ",ln=0,align="C",fill=False)
    pdf.cell(effective_page_width*0.33,0.3,txt="AUDITORY XYZ",ln=0,align="C",fill=False)
    pdf.cell(effective_page_width*0.33,0.3,txt="KINESTHETICS XYZ",ln=1,align="C",fill=False)
    pdf.ln(0.4)
    pdf.cell(effective_page_width,0.50,txt="Your Preferred Streams:-",ln=1,align="L",fill=False)
    pdf.ln(0.2)
    pdf.cell(effective_page_width*0.33,0.3,txt="SCIENCE XYZ",ln=0,align="C",fill=False)
    pdf.cell(effective_page_width*0.33,0.3,txt="COMMERCE XYZ",ln=0,align="C",fill=False)
    pdf.cell(effective_page_width*0.33,0.3,txt="ARTS XYZ",ln=1,align="C",fill=False)




    pdf.add_page()
    pdf.ln(0.3)
    pdf.set_font('Times','B',22)
    pdf.cell(effective_page_width,0.50,txt="Total finger ridge count",ln=1,align="C",fill=False)
    pdf.ln(1.6)
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(effective_page_width,0.20,txt="",align="C")
    pdf.multi_cell(effective_page_width,0.20,txt="Through  learning  mechanism  in  the  brain,  the  brain  continues  to  rewire  and  change  its  circuitry throughout our life. Therefore, learning is important to stimulate the linkage of our neurons",align="C")
    pdf.multi_cell(effective_page_width,0.20,txt="When scientists discovered einstein's brain they discovered it to be smaller than most brains ,However it had about 20 to 25% more neuron-connections  than most human brains",align="C")
    pdf.ln(1.6)
    pdf.set_font('Times','B', size=14 )
    pdf.multi_cell(effective_page_width,0.30,txt="YOUR TFRC IS XYZ",align="C")
    pdf.ln(1.6)
    pdf.multi_cell(effective_page_width,0.20,txt="The value of TFRC does not directly represents a person IQ but it is a indication of individual inborn capacity. An individual with TFRC lower than 60 needs to be patient in their learning process and get sufficient stimulation and reinforcement.",align="C")
    pdf.ln(0.5)
    pdf.multi_cell(effective_page_width,0.20,txt="Individual with TFRC 180 and above has high learning capacity and short term memory. Through learning, brain will create and organize the synaptic connections in response to extrinsic circumstances. Arch type pattern fingerprint indicates a potential value between zero to infinity. It represents that particular potential is high in plasticity",align="C")
    pdf.ln(0.5)
    pdf.image("trfc.jpg", x=None, y=None, w=5, h=3, type='', link='trfc.jpg')


    response = make_response(pdf.output(dest='S').encode('latin-1'))
    response.headers.set('Content-Disposition', 'attachment', filename=name + '.pdf')
    response.headers.set('Content-Type', 'application/pdf')
    return response

if __name__ == '__main__':
    # app.run()  
    # webbrowser.open_new_tab('http://127.0.0.1:5000/')
    app.run()  

     

# webbrowser.open_new_tab('http://127.0.0.1:5000/')
