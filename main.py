from flet import *





DIC_ANSWER={"1":"0"  ,   "2":"1",   "3":"2"  ,  "4":"3"

            ,"1-2":"5"  ,   "1-3":"6"   ,  "1-4":"7" 

            ,"2-3":"8"  ,  "2-4":"9"

            ,  "3-4":"A"

            ,  "1-2-3":"B" ,  "1-2-4":"C" ,  "1-3-4":"D" ,  "2-3-4":"E"

            ,   "1-2-3-4":"F"
            ,"-":"" , "":""}




def write_answer_on_txt_file(n,answer):
    n=str(n)
    if ".txt" not in n:
        dir_file_question=n+".txt"
    else :
        dir_file_question=n
    #write
    f=open(dir_file_question,"w")
    f.write(answer)
    f.close()

    #read()

    #write
    f=open(dir_file_question,"r")
    answer_writed=f.read()
    f.close()

    return answer_writed
    
        

def organizeAnswer(answer):
        answer_organiser=''
        answer=answer.replace(" ","")
        l=answer.split("-")
        while "" in l:
            l.remove("")
        for i in range(1,5):
            if str(i) in l:
                answer_organiser+=f"{i}-"
        answer_organiser=answer_organiser[:-1]
        if answer_organiser=="":
            answer_organiser="-"
        return answer_organiser

    

def on_click_principal(e,list_Buttons,text_answer,page):
        print("on_click_principal")
        val = e.control.text
        index=int(val)-1
        B=list_Buttons[index]

        old_color=B.bgcolor

        if  old_color=="red" :
            new_color="blue"
        if  old_color=="blue" :
            new_color="red"
            
        B.bgcolor=new_color 
        

        #generate answer
        answer=""
        for B  in list_Buttons  :
            if  B.bgcolor=="blue" :
                print(B.text)
                answer+=str(B.text)+"-"
        new_answer=organizeAnswer(answer)
        print(new_answer)

        

        #
        number_question="1"
        answer_writed=write_answer_on_txt_file(number_question ,new_answer)

        #update text_answer
        print(text_answer)
        text_answer.text=answer_writed
        

        page.update()
        
        #print(old_color)

        



def main(page:Page):

    #functions
    def changeNumberSeire(e):
        new_serie = e.control.text
        #page.appbar.bgcolor="blue"
        #page.appbar.title=new_serie  page.appbar.title={'value': '1- السلسة', 'n': 'title'}
        page.appbar.title=Text(new_serie)#['value']=new_serie
        page.update()
        print(new_serie)

    def changeNumberQuestion(e):
        new_number_question = e.control.text
        #page.appbar.bgcolor="blue"
        #page.appbar.title=new_serie  page.appbar.title={'value': '1- السلسة', 'n': 'title'}
        #page.appbar.title=Text(new_serie)#['value']=new_serie
        #page.update()
        print(new_number_question)
        

    #on_click_1
    def on_click(e):
        on_click_principal(e,list_Buttons,text_answer,page)

    def go_next_question(e):
        print("go_next_question")
        n=int(B_number_question.text.split("-")[1])
        if n<40 :
            n+=1
        #got_to_specific_question
        got_to_specific_question(n)

    def go_previeous_question(e):
        print("go_next_question")
        n=int(B_number_question.text.split("-")[1])
        if n>1 :
            n-=1

        #got_to_specific_question
        got_to_specific_question(n)

    def on_click_B_number_question(e):
        txt=e.control.text
        print(txt)
        [PopupMenuItem(text=f"السؤال-{i+1}",on_click=changeNumberQuestion) for i in range(40) ]
        
        

    def got_to_specific_question(n):
        B_number_question.text=f"السؤال-{n}"
        page.update()


    def changeWidget(e):
        print('changeWidget')
        
        index=int(e.control.selected_index)
        if index==1 :
            print("visible")
            page.add(column_answer,row_next_back)
            column_answer.visible=True
            row_next_back.visible=True

            #hide
            row_copy_save.visible=False
            text_writre_trueAnswer.visible=False
        else :
            print("hide")
            column_answer.visible=False
            row_next_back.visible=False

            #show
            row_copy_save.visible=True
            text_writre_trueAnswer.visible=True
            
            
        page.update()   
        print("index",index)

    def command_ask_yesy_no_to_save(e):
        print('command_ask_yesy_no_to_save')
        page.open(alert_dialog_save)

    def command_save_no(e):
        print('command_save_no')
        page.close(alert_dialog_save)

    def command_save_yes(e):
        print('command_save_yes')
        page.close(alert_dialog_save)

        txt=text_writre_trueAnswer.value
        print("text copied" , txt)

        #write answer
        file_answer="true_answer.txt"
        f=open(file_answer,"w")
        f.write(txt)
        f.close()

    def paste_text(e):
        txt=page.get_clipboard()
        text_writre_trueAnswer.value=txt
        page.update()

    def demarage():
        #load answer
        #read answer
        file_answer="true_answer.txt"
        try :
            f=open(file_answer,"r")
            s=f.read()
            f.close()
            #write answer on text_writre_trueAnswer
            text_writre_trueAnswer.value=s
        except :
            f=open(file_answer,"w")
            f.close()
        #page.update()
        page.update()
            

    
        
        

    
        
        

    
    
    page.title="Code Maroc Android"
    page.horizontal_alignment="center"
    page.vertical_alignment="center"
    #page.vertical_alignment = MainAxisAlignment.CENTER
    #page.horizontal_alignment = MainAxisAlignment.CENTER
    #page.padding=200
    
    



    #app appbar_seire
    page.appbar=AppBar(bgcolor="red",
                       
                       
                       title=Text("1- السلسة"),
                       center_title=True,
                       

                       actions=[
                           PopupMenuButton(
                               items=[
                                PopupMenuItem(text=f"السلسلة-{i+1}",on_click=changeNumberSeire) for i in range(40)])
                           ]
                       ,

                       #title=Text("1- السلسة"),
                       
                       
                       

                       )


    #navigation_bar
    page.navigation_bar=NavigationBar(height=60,
        on_change=changeWidget,
        selected_index=0,
        destinations=[
            NavigationBarDestination(icon=Icons.EDIT_DOCUMENT),
            NavigationBarDestination(icon=Icons.HOME)
            ]
        )


    
    
    B_with=300
    B_hieght=60
    B_number_question = FilledButton(text="السؤال-1",bgcolor="black",color="white",width=B_with, height=50
                                     ,on_click=on_click_B_number_question)

    #
    text_answer=TextButton(text="-", width=B_with, height=50)

    B1=FilledButton(text="1",bgcolor="red",width=B_with,height=B_hieght,on_click=on_click)
    B2=FilledButton(text="2",bgcolor="red",width=B_with,height=B_hieght,on_click=on_click)
    B3=FilledButton(text="3",bgcolor="red",width=B_with,height=B_hieght,on_click=on_click)
    B4=FilledButton(text="4",bgcolor="red",width=B_with,height=B_hieght,on_click=on_click)
    list_Buttons=[B1,B2,B3,B4]
    
    list_number_question_text_answser=[B_number_question,text_answer]

    B_back=FilledButton(text="<",bgcolor="black",color="white",width=int(B_with/2)-10
                        ,on_click=go_previeous_question)
    B_next=FilledButton(text=">",bgcolor="black",color="white",width=int(B_with/2)-10
                        ,on_click=go_next_question)
    #row_next_back
    row_next_back=Row(spacing=20, controls=[B_back,B_next],alignment="center")

    column_answer=Column(spacing=20, controls=list_number_question_text_answser+list_Buttons                         
                        )


    #TextAnswer
    text_writre_trueAnswer=TextField(multiline=True,min_lines=15,max_lines=15,width=400)
    
    #B_copy
    B_copy=FilledButton(text="نسخ",on_click=paste_text)

    
        

    #material_actions 
    material_actions = [
        TextButton(text="نعم",on_click=command_save_yes),
        TextButton(text="لا" , on_click=command_save_no),
    ]
    #B_save
    alert_dialog_save=AlertDialog(
                    title=Text("حفظ"),content=Text("هل تريد الحفظ ؟"),
                    actions=material_actions
                    )

    
        
    
    B_save=FilledButton(text="حفظ",on_click=command_ask_yesy_no_to_save)

    row_copy_save=Row(spacing=20, controls=[B_save,B_copy],alignment="center")

    
    

    
    #hide
    row_copy_save.visible=False
    text_writre_trueAnswer.visible=False

    #add
    page.add(column_answer,row_next_back,text_writre_trueAnswer,row_copy_save)
    
    



    #call demarage()
    demarage()
    
    #page.fullscreen=True
    page.update()


app(main)
