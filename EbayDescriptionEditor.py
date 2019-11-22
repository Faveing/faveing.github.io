import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
import json
import xml.dom.minidom
from html.parser import HTMLParser
import re
import pyperclip

forms = []

def main_screen():

    global root
    global link_entry
    global descirption
    global product_frame

    root = tk.Tk()
    root.title("SimplyInventory")
    width = 1500
    height = 1000
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenmmheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (width/2)

    root.geometry("1500x1000")
    #root.resizable(0,0)

    banner = tk.Frame(root)
    banner.pack(pady=10)

    #titleBanner = tk.Label(banner, text="Simply Inventory")
    #titleBanner.pack()
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu2 = tk.Menu(menubar, tearoff=0)
    menu3 = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=Open)
    filemenu.add_command(label="Save")
    filemenu.add_cascade(label="Quit", command=Logout)
    menubar.add_cascade(label="File", menu=filemenu)

    product_frame = tk.Frame(root)

    global product1_link
    global product2_link
    global product3_link
    global product4_link

    global product1_description
    global product2_description
    global product3_description
    global product4_description

    global product1_name
    global product2_name
    global product3_name
    global product4_name

    product1_link = tk.Entry(product_frame)
    product1_description = tk.Entry(product_frame)
    product2_link = tk.Entry(product_frame)
    product2_description = tk.Entry(product_frame)
    product3_link = tk.Entry(product_frame)
    product3_description = tk.Entry(product_frame)
    product4_link = tk.Entry(product_frame)
    product4_description = tk.Entry(product_frame)

    product1_link.grid(row=1,column=1)
    product2_link.grid(row=2,column=1)
    product3_link.grid(row=3,column=1)
    product4_link.grid(row=4,column=1)

    product1_description.grid(row=1,column=2)
    product2_description.grid(row=2,column=2)
    product3_description.grid(row=3,column=2)
    product4_description.grid(row=4,column=2)

    product1_name = tk.Entry(product_frame)
    product2_name = tk.Entry(product_frame)
    product3_name = tk.Entry(product_frame)
    product4_name = tk.Entry(product_frame)

    product1_name.grid(row=1,column=3)
    product2_name.grid(row=2,column=3)
    product3_name.grid(row=3,column=3)
    product4_name.grid(row=4,column=3)

    get_description = tk.Button(product_frame,text="Get description", command=Open)

    get_description.grid(row=5, column=1)


    # link_entry = tk.Entry(product_frame)
    # descirption = tk.Text(product_frame)
    # tk.Label(product_frame, text="Product Link:").grid(row=1, column=0)
    # tk.Label(product_frame, text="Product Description:").grid(row=2, column=0)

    # link_entry.grid(row=1, column=1)
    # descirption.grid(row=2, column=1)
    product_frame.pack()

    root.config(menu=menubar)

    main_frame = tk.Frame()

    ask_file_botton = tk.Button(text="")

def get_product_link(html, product_number, link_number):

    print("get_product_link: product_number=" + str(product_number))
    print("get_product_link: link_number=" + str(link_number))

    product = html.split("<!-- Product -->")

    # print(product)

    link = product[1].split("<!-- Image link -->")

    link = link[link_number].split("<!-- Link -->")

    link = link[1].split("'")

    return link[1]

def get_product_description(html, product_number, description_number):
    product = html.split("<!-- Product -->")

    product_description = product[product_number].split("<!-- Description Text-->")

    return product_description[description_number]

def create_new_product_section():
    link_entry = tk.Entry(product_frame)
    descirption = tk.Text(product_frame)

    combined = []

    combined.append(link_entry)
    combined.append(descirption)

    forms.append(combined)

def draw_forms():

    print(forms)

    for i in range(len(forms)):
        for x in range(len(forms[i])):
            forms[i][x].grid(row=x, column=i)

    # link_entry.grid(row=1, column=1)
    # descirption.grid(row=2, column=1)

def fill_forms(html):

    for i in range(len(forms)):
        for x in range(len(forms)):
            print("fill_forms: forms[" + str(i) + "][" + str(x) + "]=" + str(forms[i][1]))

    print("fill_forms: length if forms" + str(len(forms)))
    print("fill_forms: length of forms[i] " + str(len(forms)))

    for i in range(len(forms)):
        for x in range(len(forms[i])):
            link = get_product_link(html, i, x)    
            forms[i][x].insert("0", link)        

def edit_template(main_description, description_image, product1_link, product1_description,product2_link, product2_description, product3_link, product3_description,product4_link, product4_description):

    newhtml = """  
<html>
	<title>eBay</title>


	<style>
		/* -------------------------------------------------- 
		eBay Global
		-------------------------------------------------- */
		body																			{ margin:0 2px !important; padding:0 !important; }
		.stBadge																		{ min-width: 320px; max-width:100%; }
		.su-bg																			{ width:100% !important; }
		.su-bg *																		{ margin:0; padding:0; vertical-align:top; font-size: 20px; }
		.su-bg img																	{ border:0; }
		.su-bg-02																	{ width:100%; max-width:100%; padding:0; display:block; }
		.su-bg, .su-bg-02, .su-content									{ margin:0 auto; text-align:center; vertical-align:top; }
		@media screen and (max-width:1020px) 					{ .su-bg .su-nota { display:none !important; } }
		@media screen and (max-width:700px) 					{ .su-bg .su-nomo { display:none !important; } }
		.su-content, #su-head, #su-foot, .su-vaca    		{ position:relative; margin:0 auto; }
		#su-head-wrap, #su-foot-wrap				    			{ width:100%; position:relative; margin:0 auto; }
		.su-content, #su-head, #su-foot    							{ width:100%; }
		.su-content																{ padding:15px 0 10px !important; }
		.su-content tr:first-child td[colspan="3"][height="15"]	,
		.su-bg td [width="13"]												{ display:none !important; }
		#CentralArea, .su-content,
		#su-template #su-main,
		.su-bg .su-sbox, #su-deal,
		.su-bg .su-tbox, .su-bg .su-pbox,
		.su-bg #LeftPanel .su-tins,
		.su-bg #su-main .su-tins, .su-foot-tins,
		.su-bg .su-prom, .su-bg .su-prot,
		#LeftPanel .su-ttba, #su-main .su-ttba,
		.su-bg #su-head-mnav .su-mbox label,
		.su-bg #su-head-mnav .su-mnav,
		#su-main-fcat a, .su-bg #su-main #su-main-feed,
		#su-foot-main .su-foot-cols, #su-foot-copy			{ box-sizing: border-box; -moz-box-sizing: border-box; -webkit-box-sizing: border-box; }
		#su-template #su-main,
		.su-bg .su-sbox, #su-deal,
		.su-bg .su-tbox, .su-bg .su-pbox,
		.su-bg #RightPanel .su-tins,
		.su-bg #su-main .su-tins, .su-foot-tins,
		.su-bg .su-prom, .su-bg .su-prot,
		#LeftPanel .su-ttba, #su-main .su-ttba,
		.su-bg #su-head-mnav .su-mbox label,
		.su-bg #su-head-mnav .su-mnav,
		#su-main-fcat a, .su-bg #su-main #su-main-feed,
		#su-foot-main .su-foot-cols, #su-foot-copy			{ box-sizing: border-box; -moz-box-sizing: border-box; -webkit-box-sizing: border-box; }
		.su-bg .su-content-width											{ width:100%; margin:0 auto; }
		.su-bg, .su-bg-02, .su-content,
		.su-bg .su-content-width,
		.su-bg #LeftPanel, .su-bg #su-main,
		#su-head-wrap-01, #su-head-wrap-02,
		#su-head-wrap-03, #su-head-wrap-04, 
		.su-bg .su-bklt,
		.su-bg #su-head-srch, .su-bg #su-side-srch,
		.su-bg #su-head-tnav, #su-head-menu,
		.su-bg #su-head-mnav, 
		#su-deal, #su-deal #su-feat,
		#su-deal #su-feat .su-fp a .title,
		.su-bg .su-prom.su-prot,
		#su-side-feat #su-feat,
		#su-side-feat #su-feat .su-fp a span,
		#su-side-feed, #su-main #su-main-whys,
		#su-main #su-main-mini, #su-main-fcat,
		#su-main-feat #su-feat,
		#su-main-feat #su-feat .su-fp a,
		#su-main-feat #su-feat .su-fp a span,
		#su-main h2, #su-temp-gall,
		.su-bg #LeftPanel .su-tins,
		.su-bg #su-main .su-tins, .su-foot-tins,
		#su-foot-subm, #su-foot-copy,
		#su-foot-main .su-foot-cols,
		#su-foot-copy p														{ overflow:hidden; }
		#LeftPanel, #LeftPanel .su-tbar, 
		#LeftPanel .su-ttop, #LeftPanel .su-tmid, 
		#LeftPanel .su-tbtm, #LeftPanel .su-prom,
		#CentralArea, #su-main, #su-main-fcat, 
		#su-main-feat, #su-main .su-tbar, 
		#su-main .su-ttop, #su-main .su-tmid, 
		#su-main .su-tbtm, #su-main-tabs			       	 		{ display:block; overflow:hidden; background:transparent none; }
		.su-bg .su-content-width											{ width:100%; margin:0 auto; }
		.su-bg, .su-bg-02, .su-content,
		.su-bg .su-content-width,
		.su-bg #RightPanel, .su-bg #su-main,
		#su-head-wrap-01, #su-head-wrap-02,
		#su-head-wrap-03, #su-head-wrap-04, 
		.su-bg .su-bklt,
		.su-bg #su-head-srch, .su-bg #su-side-srch,
		.su-bg #su-head-tnav, #su-head-menu,
		.su-bg #su-head-mnav, 
		#su-deal, #su-deal #su-feat,
		#su-deal #su-feat .su-fp a .title,
		.su-bg .su-prom.su-prot,
		#su-side-feat #su-feat,
		#su-side-feat #su-feat .su-fp a span,
		#su-side-feed, #su-main #su-main-whys,
		#su-main #su-main-mini, #su-main-fcat,
		#su-main-feat #su-feat,
		#su-main-feat #su-feat .su-fp a,
		#su-main-feat #su-feat .su-fp a span,
		#su-main h2, #su-temp-gall,
		.su-bg #LeftPanel .su-tins,
		.su-bg #su-main .su-tins, .su-foot-tins,
		#su-foot-subm, #su-foot-copy,
		#su-foot-main .su-foot-cols,
		#su-foot-copy p														{ overflow:hidden; }
		#RightPanel, #RightPanel .su-tbar, 
		#RightPanel .su-ttop, #RightPanel .su-tmid, 
		#RightPanel .su-tbtm, #RightPanel .su-prom,
		#CentralArea, #su-main, #su-main-fcat, 
		#su-main-feat, #su-main .su-tbar, 
		#su-main .su-ttop, #su-main .su-tmid, 
		#su-main .su-tbtm, #su-main-tabs			       	 		{ display:block; overflow:hidden; background:transparent none; }
		#CentralArea, #su-main                       					{ margin:0 !important; float:right; vertical-align:top; }
		#CentralArea #su-main											{ padding:0 !important; }
		#LeftPanel																	{ margin:0 !important; float:left; vertical-align:top !important; background-color:transparent; }
		#RightPanel																	{ margin:0 !important; float:right; vertical-align:top !important; background-color:transparent; }
		#LeftPanel .su-temp,
		#su-template #LeftPanel .su-home              			{ display:none !important; }
		#RightPanel .su-temp,
		#su-template #RightPanel .su-home              			{ display:none !important; }
		#su-template #LeftPanel .su-temp              			{ display:block !important; }
		#su-template #RightPanel .su-temp              			{ display:block !important; }
		#CentralArea .r3, .fpcc span.keywordClass			{ background-color:#FFF; }
		#CentralArea .r3_cm					        					{ padding:10px; }
		#CentralArea .ctrlbr												{ padding:3px 10px; }
		#CentralArea .cmpBr					        					{ padding:0 10px; }
		#CentralArea span.pdmt img		            				{ vertical-align:middle; }
		#CentralArea span.tpr, #CentralArea a.tpr			{ font-size:11px; line-height:15px; padding-top:0; padding-bottom:0; }
		#TopPromoArea							   							{ display:none !important; margin:0 !important; padding:0 !important; }
		.su-bg .su-ctr                                								{ text-align:center !important; margin:0 auto !important; max-width:1400px !important; }
		#su-head .ttl, #su-head .link, #su-head .all_cats,
		#su-head .cnt, #su-head .v4acpcont,
		#su-head-mnav .ttl, #su-head-mnav .link,
		#su-head-mnav .all_cats, 
		#su-head-mnav .cnt, 
		#su-head-mnav .v4acpcont,
		#su-head-mnav ul.lev1 li br, 
		#su-head-mnav ul.lev2 li br,
		#LeftPanel .ttl, #LeftPanel .link,
		#LeftPanel .all_cats, 
		#LeftPanel .cnt, 
		#LeftPanel .v4acpcont,
		#su-side-cats ul.lev1 li br, 
		#su-side-cats ul.lev2 li br, .su-hide							{ display:none !important; }
		#RightPanel .ttl, #RightPanel .link,
		#RightPanel .all_cats, 
		#RightPanel .cnt, 
		#RightPanel .v4acpcont,
		#su-side-cats ul.lev1 li br, 
		#su-side-cats ul.lev2 li br, .su-hide							{ display:none !important; }
		.su-bg .su-ffbn, .su-bg a.su-ffbn,
		.su-bg #su-head-tnav a,
		.su-bg #su-head-mnav .su-mnav ul li a,
		.su-bg #su-head-wrap-02 #su-head-menu a,
		.su-bg #su-head-wrap-03 #su-head-menu a,
		.su-bg #su-head-whys img,
		.su-bg #LeftPanel .lev1 li a, 
		.su-bg #LeftPanel .lev1 li span,
		.su-bg #LeftPanel .su-prot,
		.su-bg #su-main .su-prot,
		#su-main-fcat a, #su-main-feat #su-feat .su-fp,
		#su-main-feat #su-feat .su-fp a,
		#su-temp-gall #su-gall-thmb .su-hold,
		#su-foot-subm a, #su-foot-copy a,
		#su-foot-main .su-foot-cols ul li,
		#su-foot-main .su-foot-cols ul li a,
		#su-foot-main .su-foot-cols #su-foot-cont a			{ -webkit-transition:0.5s ease-in-out; transition:0.5s ease-in-out; }
		.su-bg .su-ffbn, .su-bg a.su-ffbn,
		.su-bg #su-head-tnav a,
		.su-bg #su-head-mnav .su-mnav ul li a,
		.su-bg #su-head-wrap-02 #su-head-menu a,
		.su-bg #su-head-wrap-03 #su-head-menu a,
		.su-bg #su-head-whys img,
		.su-bg #RightPanel .lev1 li a, 
		.su-bg #RightPanel .lev1 li span,
		.su-bg #RightPanel .su-prot,
		.su-bg #su-main .su-prot,
		#su-main-fcat a, #su-main-feat #su-feat .su-fp,
		#su-main-feat #su-feat .su-fp a,
		#su-temp-gall #su-gall-thmb .su-hold,
		#su-foot-subm a, #su-foot-copy a,
		#su-foot-main .su-foot-cols ul li,
		#su-foot-main .su-foot-cols ul li a,
		#su-foot-main .su-foot-cols #su-foot-cont a			{ -webkit-transition:0.5s ease-in-out; transition:0.5s ease-in-out; }
		#su-head-wrap-01, #su-head-wrap-02,
		#su-head-wrap-03, #su-head-wrap-04					{ width:100%; clear:both; }
		.su-bg #su-head-srch input										{ outline:none; }
		.su-tmid, .su-tmid p, .su-tmid li              					{ text-align:left; line-height:18px; }
		#CentralArea p, #su-main p, #su-main .su-tins ul,
		#su-main .su-tmid ul, #su-main .su-tbox ul				{ padding:0 0 15px; }
		#CentralArea ul, #su-head ul, #foot ul,
		#LeftPanel ul, #su-main ul		            					{ list-style-type:none; }
		#RightPanel ul, #su-main ul		            					{ list-style-type:none; }
		#CentralArea li, #su-main li				    					{ padding:0 0 5px 15px; }
		#su-head-menu li	                            						{ display:inline; float:left; background:transparent none; padding:0; }
		#su-main .su-tmid ol													{ padding:0 15px 15px 25px; }
		#su-main .su-tmid ol li												{ background:transparent none; padding:0 0 5px 0; }
		#su-head *, #su-foot *, 
		#LeftPanel *, #su-main *                     						{ text-decoration:none; }
		#RightPanel *, #su-main *                     						{ text-decoration:none; }
		#su-main .su-tmid a, #su-main .su-tmid a:link,
		#su-main .su-tmid a:active, 
		#su-main .su-tmid a:visited, 
		#su-main .su-tmid a:hover										{ text-decoration:underline; }
		#su-head-srch-bttn, #su-head-menu li,
		#LeftPanel li, #su-side-news-bttn, 
		#su-main-tabs img, #su-gall-thmb img      				{ cursor:pointer; }
		#RightPanel li, #su-side-news-bttn, 
		#su-main-tabs img, #su-gall-thmb img      				{ cursor:pointer; }
		#RightPanel ul li a, #RightPanel ul li span,
		#su-main-fcat a, #su-main-fcat a img,
		.su-bg #LeftPanel .lev1 li,
		.su-bg #LeftPanel .lev2 li,
		.su-bg #LeftPanel .lev3 li
		#su-main-tabs img, #su-main-feat .su-fp *       		{ display:block; }
		.su-bg #RightPanel .lev1 li,
		.su-bg #RightPanel .lev2 li,
		.su-bg #RightPanel .lev3 li
		#su-main-tabs img, #su-main-feat .su-fp *       		{ display:block; }
		.su-bg .su-sbox, .su-bg .su-sbox p, 
		.su-bg .su-sbox a, .su-bg .su-sbox li,
		.su-bg .su-tbox, .su-bg .su-tbox p, 
		.su-bg .su-tbox a, .su-bg .su-tbox li, 
		.su-bg .su-pbox, .su-bg .su-pbox p,
		.su-bg .su-pbox a, .su-bg .su-pbox li 						{ text-align:left; padding-top: 2px; text-align: left;}
		.su-bg #su-main ul														{ list-style-type:disc; margin-left:20px; padding-left:0px; list-style-position:outside; }
		.su-bg #su-main ul li													{ padding:0 0 8px; }
		.su-bg #su-main ol														{ margin-left:10px; margin-bottom:15px; padding-left:10px; }
		.su-bg #su-main ol li													{ padding-left:5px; }
		.su-bg .su-sbox, #su-deal, .su-bg .su-tbox,
		.su-bg .su-pbox															{ width:auto; margin:0 0 15px; }
		.su-bg .su-prom															{ display:block; margin:0 auto 15px; width:auto; max-width:100%; height:auto; }
		.su-bg .su-prom.su-prot											{ width:100%; }
		@media screen and (max-width:500px) 					{ .su-bg #su-main .su-prom { display:none; }  .su-bg #su-main .su-prom.su-prot { display:block; } }
		#LeftPanel .su-ttba, #su-main .su-ttba					{ width:auto; text-align:left; margin:0; }
		#RightPanel .su-ttba, #su-main .su-ttba					{ width:auto; text-align:center; margin:0; }
		.su-bg .su-ttba .su-tins												{ padding:0 !important; }
		.su-bg .su-ffbn, .su-bg a.su-ffbn								{  -webkit-border-radius:0; border-radius:0; -webkit-appearance:none; }
		#su-main-feat #su-feat												{ padding:0; text-align:center; }
		#su-main-feat #su-main-feat-pull,
		#su-main-feat #su-main-fea2-pull,
		#su-main-feat #su-main-fea3-pull,
		#su-main-feat #su-main-fea4-pull							{ display:none; }
		#LeftPanel #su-left-spacer.su-prom,
		#su-main #su-home-spacer.su-prom						{ margin-bottom:0; }
		#RightPanel #su-left-spacer.su-prom,
		#su-main #su-home-spacer.su-prom						{ margin-bottom:0; }
		.su-bg .su-proh															{ width:auto; max-width:300px; }
		.su-bg .su-proh img													{ width:auto; max-width:300px; display:block; margin-left:auto; margin-right:auto; }
		.su-bg .su-proh span													{ display:block; }
		.su-bg .su-proh.su-prol												{ float:left; }
		.su-bg .su-proh.su-prom											{ margin:0 auto; }
		.su-bg .su-proh.su-pror												{ float:right; }
		.su-bg #su-head-logo.su-proh,
		.su-bg #su-head-logo.su-proh img							{ max-width:100%; }
		@media screen and (max-width:1440px)					{ .su-bg .su-proh.su-prol, .su-bg #su-head-logo.su-prol { margin-left:10px; } .su-bg .su-proh.su-pror { margin-right:10px; } }
		@media screen and (max-width:1020px)					{ .su-bg .su-proh.su-prol, .su-bg .su-proh.su-prom, .su-bg .su-proh.su-pror { float:none; margin:10px auto; } }
		@media screen and (max-width:350px)					{ .su-bg .su-proh, .su-bg #su-head-logo.su-proh, .su-bg .su-proh img { width:auto; max-width:90%; } }
		.su-bg #su-head-srch, .su-bg #su-head-mnav		{ width:300px; max-width:300px; }
		@media screen and (max-width:350px)					{ .su-bg #su-head-srch, .su-bg #su-head-mnav { max-width:90%; } }
		/* -------------------------------------------------- 
		eBay Template
		-------------------------------------------------- */
		/* single image */
		#su-gall-main.su-solo												{ text-align:center; margin:0 auto 8px; overflow:hidden; } /* single image no gallery */
		#su-gall-main.su-solo img											{ width:auto; max-width:100%; height:auto; margin:0 auto; display:block; box-sizing: border-box; -moz-box-sizing: border-box; -webkit-box-sizing: border-box; }
		@media screen and (max-width:700px)					{ #su-gall-main.su-solo img { width:99%; } }
		@media screen and (max-width:500px)					{ #su-gall-main.su-solo img { max-width:300px; } }
		/* description float right */
		#su-gall-right																{ /*width:42%;*/ float:left; overflow:hidden; background:transparent none; } /* right float description */
		.su-bg #su-gall-right .su-tins.su-text						{ background-color:#FFF; }
		#su-gall-right.su-wide												{ width:52%; float:right; overflow:hidden; }
		#su-gall-right #su-main-desc									{ width:100%; }
		#su-gall-right #su-main-spec									{ width:100%; float:none; margin:15px 0 8px; }
		@media screen and (max-width:1420px)					{ #su-gall-right { /*width:42%;*/ } #su-gall-right.su-wide { width:52%; } }
		@media screen and (max-width:860px)					{ #su-gall-right, #su-gall-right.su-wide { width:100%; float:none; margin-bottom:2px; } }
		/* image gallery general */
		#su-temp-gall,
		#su-temp-gall #su-gall-main,
		#su-temp-gall #su-gall-thmb									{ width:100%; height:auto; text-align:center; margin:0 auto; overflow:hidden; line-height:1px; } /* gallery with thumbs bottom */
		#su-temp-gall .su-cntr												{ width:100%; height:100%; background:#FFF none; vertical-align:middle; text-align:center; overflow:auto; }
		#su-temp-gall img														{ margin:0 auto; display:block; border:0 none; width:auto; height:auto; }
		#su-temp-gall #su-gall-main										{ background:#FFF none; margin-bottom:10px; position:relative; }
		#su-temp-gall #su-gall-main img								{ width:auto; max-width:100%; height:auto; max-height:100%; margin:0 auto; }
		#su-temp-gall #su-gall-thmb h5								{ font-size:12px; font-weight:normal; text-align:center; margin:0; padding:0 0 5px; width:100%; clear:both; padding-top: 9px;}
		#su-temp-gall #su-gall-thmb h5 span						{ display:inline-block; width:18px; height:18px; background-color:transparent; background-position:left center; background-repeat:no-repeat; }
		#su-temp-gall #su-gall-thmb .su-hold						{ width:100px; height:100px; background:#FFF none; margin:3px 2px; display:inline-block; }
		#su-temp-gall #su-gall-thmb img								{ max-width:90px; max-height:90px; }
		#su-temp-gall .su-hide 												{ display:none !important; }
		/* #su-temp-gall #su-gall-thmb div[class*=" nt-hide"]	{ display:none !important; }
		#su-temp-gall #su-gall-thmb div[class*=" nt-hidehttps"]	{ display:inline-block !important; } */
		#su-temp-gall #su-gall-main > div[id^="mimg"]		{ position:absolute; width:100%; height:100%; top:0; left:0; right:0; bottom:0; z-index:0; }
		#su-temp-gall #su-gall-main > div:target				{ z-index:2; }
		/* gallery thumbs bottom */
		#su-temp-gall.su-bttm												{ max-width:600px; margin-bottom:8px; }
		#su-temp-gall.su-bttm #su-gall-main						{ padding-top:100%; box-sizing:border-box; -moz-box-sizing:border-box; -webkit-box-sizing:border-box; }
		/* gallery thumbs side */
		#su-temp-gall.su-side												{ max-width:85%; margin-bottom:8px; }
		#su-temp-gall.su-side #su-gall-main						{ max-width:600px; padding-top:69.51%; float:left; }
		#su-temp-gall.su-side #su-gall-thmb						{ width:210px; float:right; }
		#su-temp-gall.su-side #su-gall-thmb h5					{ padding:0; }
		#su-temp-gall.su-side.su-wide									{ max-width:902px; } /* 1 col layout with full width side thumbs gallery */
		#su-temp-gall.su-side.su-wide #su-gall-main			{ max-width:700px; padding-top:69.51%; }
		@media screen and (max-width:1340px)					{ #su-temp-gall.su-side, #su-temp-gall.su-side.su-wide { max-width:85%; } }
		@media screen and (max-width:1270px)					{ #su-temp-gall.su-side, #su-temp-gall.su-side.su-wide { max-width:90%; } }
		@media screen and (max-width:1220px)					{ #su-temp-gall.su-side, #su-temp-gall.su-side.su-wide { max-width:95%; } }
		@media screen and (max-width:1160px)					{ #su-temp-gall.su-side, #su-temp-gall.su-side.su-wide { max-width:100%; } }
		@media screen and (max-width:1090px)					{ #su-temp-gall.su-side #su-gall-main { max-width:69.51%; } }
		#su-temp-gall.su-side.su-700									{ max-width:90%; }  /* 2 col layout with enlarged side thumbs gallery */
		#su-temp-gall.su-side.su-700 #su-gall-main			{ max-width:700px; padding-top:72.08%; }
		@media screen and (max-width:1370px)					{ #su-temp-gall.su-side.su-700 { max-width:95%; } }
		@media screen and (max-width:1290px)					{ #su-temp-gall.su-side.su-700 { max-width:90%; } #su-temp-gall.su-side.su-700 #su-gall-main { max-width:600px; padding-top:69.51%; } }
		@media screen and (max-width:1220px)					{ #su-temp-gall.su-side.su-700 { max-width:95%; } }
		@media screen and (max-width:1160px)					{ #su-temp-gall.su-side.su-700 { max-width:100%; } }
		@media screen and (max-width:860px) { 
		#su-temp-gall.su-side, #su-temp-gall.su-side.su-wide,
		#su-temp-gall.su-side.su-700									{ max-width:500px; } 
		#su-temp-gall.su-side #su-gall-main,
		#su-temp-gall.su-side.su-700 #su-gall-main,
		#su-temp-gall.su-side.su-wide #su-gall-main			{ width:100%; max-width:100%; float:none; padding-top:100%; box-sizing:border-box; -moz-box-sizing:border-box; -webkit-box-sizing:border-box; }
		#su-temp-gall.su-side #su-gall-thmb						{ width:100%; max-width:100%; float:none; }
		#su-temp-gall.su-side #su-gall-thmb h5					{ padding:0 0 5px; }
		}
		#su-gall-main.su-solo.su-left,
		#su-temp-gall.su-bttm.su-left,
		#su-temp-gall.su-bttm.su-wide								{ float:none; } /* single image or gallery left with right float description */
		/* #su-gall-main.su-solo.su-left,
		#su-temp-gall.su-bttm.su-left									{ width:56.7%; max-width:56.7%; } */
		#su-gall-main.su-solo.su-left.su-wide,
		#su-temp-gall.su-bttm.su-wide								{ width:auto; max-width:602px; }
		/* @media screen and (max-width:1420px)					{ #su-gall-main.su-solo.su-left, #su-gall-main.su-solo.su-left.su-wide, #su-temp-gall.su-bttm.su-left, #su-temp-gall.su-bttm.su-wide { width:56%; } } */
		@media screen and (max-width:860px) {
		#su-gall-main.su-solo.su-left,
		#su-temp-gall.su-bttm.su-left,
		#su-temp-gall.su-bttm.su-wide								{ float:none; width:100%; max-width:600px; margin-bottom:20px; }
		#su-gall-right																{ width:100%; float:none; margin-bottom:2px; }
		}
		#su-gall-main [type="radio"]									{ display:none; } /* selection and alignment */
		#su-gall-main [type="radio"] ~ div.su-cntr				{ display:inline-block; opacity:0; filter:alpha(opacity=0);  transition: 0.5s; }
		#su-gall-main [type="radio"]:checked ~ div.su-cntr { opacity:1; filter:alpha(opacity=100); }
		#su-gall-main [type="radio"] ~ div.su-cntr img		{ margin:auto !important; left:0; right:0; top:0; bottom:0; position:absolute; }
		#su-gall-main [type="radio"] ~ div.su-cntr img				{ opacity:0; filter:alpha(opacity=0);  }
		#su-gall-main [type="radio"]:checked ~ div.su-cntr img { opacity:1; filter:alpha(opacity=100); }
		#su-gall-thmb label div.su-cntr								{ position:relative; }
		#su-gall-thmb label div.su-cntr img							{ margin:auto !important; left:0; right:0; top:0; bottom:0; position:absolute; }
		.su-bg #su-main #su-main-tabs								{ width:100%; height:auto; position:relative; clear:both; margin:0 0 15px; overflow:hidden; }
		.su-bg #su-main #su-main-tabs .su-tbox					{ margin:0; max-height:320px; overflow:auto; }
		.su-ttab																		{ float:none; }
		.su-ttab label																{ width:100%; position:relative; left:0; display:block; cursor:pointer; }
		.su-ttab [type=radio]												{ display:none; }
		.su-ttrm																		{ top:0; left:0; right:0; bottom:0; position:relative; }
		.su-bg #su-main [type=radio]:checked ~ label.su-bktt	{ z-index:2; }
		[type=radio] ~ label.su-bktt ~ .su-ttrm					{ display:none; }
		[type=radio]:checked ~ label.su-bktt ~ .su-ttrm	{ display:block; z-index:1; }
		.su-bg span.su-copy-ninja a											{ padding-right:24px; margin-right:4px; font-weight:normal; background:transparent url(images/nt-favicon-16.png) right center no-repeat; }
		.su-bg span.su-copy-ninja2 a,
		.su-bg span.su-copy-ninja2 span									{ padding-left:24px; margin-left:4px; font-weight:normal; background:transparent url(images/nt-favicon-16.png) left center no-repeat; display:inline-block; }
		/* -------------------------------------------------- 
		eBay Category
		-------------------------------------------------- */
		.su-bg .v4stabl, .su-bg .v4stabl a								{ font-size:11px; }
		.su-bg .v4stabl a:hover											{ text-decoration:underline; }
		.su-bg #CentralArea .r3, .su-bg .r3_c,
		.su-bg .r3_t, .su-bg .r3_t b, .su-bg .r3_t i,
		.su-bg .r3_bl, .su-bg .r3_bl b, .su-bg .r3_bl i,
		.su-bg .cmpBr, .su-bg table.pgbc, .su-bg .rs_box,
		.su-bg .ctrlbr, .su-bg td#CentralArea div.dynpg,
		.su-bg .fpcc span.keywordClass								{ background-color:transparent; background-image:none; border-left:0; border-right:0; border-top:0; border-bottom:0; }
		.su-bg .r3_cm.bp.tp													{ }
		.su-bg .ctrlbr																{ margin-bottom:5px; }
		.su-bg .fpcc .countClass,
		.su-bg .fpcc .matchClass,
		.su-bg .fpcc .keywordClass										{ font-size:13px; line-height:18px; }
		.su-bg .fpcc .countClass											{ font-size:15px; }
		.mn .sel, .mn li a:hover, .mn li a:focus, 
		.mn li a:active															{background-color:#EEE; }
		.su-bg td#CentralArea span.pdmt:first-child		{ display:none; }						
		.su-bg td#CentralArea span.pdmt span					{ font-size:13px; line-height:18px; }
		.su-bg td#CentralArea span.pdmt span.label			{ }
		.su-bg td#CentralArea span.pdmt span.cur			{ padding-right:15px; background:transparent url(images/nt-cate-drop.png) right 2px no-repeat; }
		.su-bg td#CentralArea span.pdmt span.cur img	{ display:none; }
		.su-bg .cmpBr .cmsg, .su-bg .cmpBr .cmsg a			{ font-size:12px; line-height:16px; }
		.su-bg .cmpBr .cmsg a:hover									{ text-decoration:underline; }
		#su-main-cate															{ overflow:hidden; padding:0 0 10px; text-align:center; }
		#su-main-cate, #products-layout							{ width:100%; }
		#su-main-cate .su-fp												{ width:162px; height:330px; background:#FFF none; margin:20px 10px 0; padding:10px 15px; display:inline-block; position:relative; overflow:hidden; }
		@media screen and (max-width:1180px) 					{ #su-main-cate .su-fp { width:156px; margin:10px 4px; padding:10px; } }
		#su-main-cate .su-fp a,
		#su-main-cate .su-fp a span										{ text-align:left; font-size:13px; line-height:15px; display:block; overflow:hidden; }
		#su-main-cate .su-fp a .thumb									{ width:168px; height:160px; display:block; display:table-cell; vertical-align:middle; text-align:center; }
		#su-main-cate .su-fp a .thumb img							{ max-height:140px; width:auto; max-width:140px; margin:0 auto 10px; border:0 none; }
		#su-main-cate .su-fp a .title									{ height:45px; margin:0 0 10px; text-align:center; }
		#su-main-cate .su-fp a .title:hover						{ }
		#su-main-cate .su-fp .subtitle									{ color:#999; font-size:12px; line-height:14px; margin:0 0 10px; display:block; }
		#su-main-cate .su-fp .price,
		#su-main-cate .su-fp .price-bin,
		#su-main-cate .su-fp .bid-price								{ font-size:13px; line-height:18px; font-weight:bold; display:block; text-align:center; margin:0 0 10px; }
		#su-main-cate .su-fp .price										{ color:#999; display:none; }
		#su-main-cate .su-fp .price-bin,
		#su-main-cate .su-fp .bid-price								{ }
		#su-main-cate .su-fp .orig-price								{ color:#999; font-size:13px; line-height:16px; text-decoration:line-through; margin:0 0 2px; display:block; }
		#su-main-cate .su-fp .orig-price:before				{ content:"Original Price: " }
		#su-main-cate .su-fp .sale										{ display:block; text-align:right; position:absolute; right:10px; top:10px; }
		#su-main-cate .su-fp .bids-number,
		#su-main-cate .su-fp .discount								{ color:#FF0000; font-size:13px; line-height:16px; font-weight:bold; display:block; }
		#su-main-cate .su-fp .time-left,
		#su-main-cate .su-fp .shipping								{ color:#999; font-size:12px; line-height:18px; display:block; text-align:center; margin:0 0 10px; }
		#su-main-cate .su-fp .button									{ width:84px; height:30px; background:transparent url(images/nt-cate-bttn.png) 0 0 no-repeat; text-align:center; margin:0 auto; display:block; position:absolute; bottom:15px; left:50%; margin-left:-42px; }
		.su-bg table.pgbc														{ padding:5px 0; }
		.su-bg table.pgbc table.pager									{ margin:0 auto !important; }
		.su-bg table.pgbc td.l												{ padding:0 0 0 10px !important; width:30% !important; }
		.su-bg table.pgbc td.r												{ padding:0 10px 0 0 !important; width:30% !important; }
		.su-bg .dynpg .prev a:first-child,
		.su-bg .dynpg .next a:last-child								{ display:none !important; }
		.su-bg .dynpg .prev, .su-bg .dynpg .prev a,
		.su-bg .dynpg .next, .su-bg .dynpg .next a				{ height:18px !important; line-height:18px !important; overflow:hidden !important; }
		.su-bg .dynpg .prev a, .su-bg .dynpg .next a			{ display:block; }
		.su-bg .dynpg .prev a												{ background:transparent url(https://cdn3.vectorstock.com/i/1000x1000/60/42/black-metallic-background-vector-18826042.jpg) left bottom no-repeat !important; padding:0 0 0 25px !important; }
		.su-bg .dynpg .next a												{ background:transparent url(images/nt-cate-next.png) right bottom no-repeat !important; padding:0 25px 0 0 !important; }
		.su-bg .dynpg .prev a.enabled:hover						{ background-position:left top !important; }
		.su-bg .dynpg .next a.enabled:hover						{ background-position:right top !important; }
		.su-bg .dynpg .r .form												{ margin:0 !important; padding:0 !important; }
		.su-bg .dynpg .r .form input#q_9								{ }
		.su-bg .dynpg .r .form input#q_10							{ cursor:pointer; }
		.su-bg .dynpg .r .form input#q_10							{ width:35px; height:18px; border:0 !important; line-height:18px !important; background:transparent url(images/nt-cate-btgo.png) 0 0 no-repeat !important; }
		@media screen and (max-width:680px) 					{ .su-bg table.pgbc td.l, .su-bg table.pgbc td.r { display:none !important; } }
		.su-bg .g-hdn																{ display:none; }
		.su-bg #CentralArea .r3_cm									{ padding:5px 0 !important; }
		#su-copy-date:after												{ content:"2019"; }	
	</style>


	<style>
		/* accent 03C2B2 */
		/* main bg 2B2B2B */
		/* font 353535 */
		/* border 000 */
		/* main font "Ropa Sans" */
		/* accent font Exo */
		/* ---------------------------------------- 
		eBay Global
		---------------------------------------- */
		.su-bg																			{ background: black fixed; background-size: cover; }
		.su-bg-02, .su-content, 
		.su-bg .su-content-width, #su-head, #su-foot		{ max-width:1400px; }
		.su-bg-02																	{ max-width:100% }
		@media screen and (max-width:1440px)					{ .su-bg-02 { max-width:100%; } }
		/* --- BEG DIMENSIONS 2 COL NO SIDE MARGINS --- */
		#LeftPanel																	{ width:100% !important; max-width:280px !important; }
		#su-template #LeftPanel											{ width:20% !important; }
		#LeftPanel .su-tbar, 
		#LeftPanel .su-main-ttop, #LeftPanel .su-tmid, 
		#LeftPanel .su-tbtm									     		 	{ width:100%; max-width:280px !important; }
		@media screen and (max-width:1020px) 					{ #LeftPanel { display:none !important; } }
		#RightPanel																	{ width:100% !important; max-width:280px !important; }
		#su-template #RightPanel											{ width:25% !important; padding-left: 20px; padding-right: 15px;}
		#RightPanel .su-tbar, 
		#RightPanel .su-main-ttop, #RightPanel .su-tmid, 
		#RightPanel .su-tbtm									     		 	{ width:100%; max-width:280px !important; }
		@media screen and (max-width:1020px) 					{ #RightPanel { display:none !important; } }
		#CentralArea 															{ width:100%; max-width:1105px !important }
		@media screen and (min-width:1440px) 					{ #CentralArea { min-width:1105px; } }
		#CentralArea #su-main											{ width:100%;}
		#su-template #su-main												{ width:50%; max-width:1105px !important; }
		#LeftPanel																	{ margin:0 0 0 0px !important; }
		#RightPanel																	{ margin:0 0 0 0px !important; }
		#CentralArea, #su-main                       					{ margin:0 0px 0 0 !important; }
		#CentralArea #su-main											{ margin:0 !important; }
		@media screen and (max-width:1440px)					{ #CentralArea { padding-left:15px; } }
		@media screen and (max-width:1020px)					{ #CentralArea, #su-template #su-main { width:98%; max-width:1000px !important; margin:0 auto !important; padding:0 5px !important; float:none; } #CentralArea #su-main { width:100%; } }
		/* --- END DIMENSIONS 2 COL NO SIDE MARGINS --- */
		.su-bg *                                     									{ font-family:"Ropa Sans", sans-serif; text-decoration:none; } /* fonts */
		.su-bg, .su-bg p, .su-bg a, .su-bg li, .su-bg table,
		.su-bg form select														{ font-size:12px; line-height:20px; color:black; word-wrap:break-word; }
		/* .su-bg a:link, .su-bg a:visited, .su-bg a:active		{ color:#FFF; } */
		.su-bg a:hover							            					{ color:#03C2B2; }
		#CentralArea h1, #su-main h1								{ color:black; text-align:center; font-size:22px; line-height:26px; font-weight:bold; font-style:italic; margin:0; padding:0 0 15px; }
		#CentralArea h5, #su-main h5		            			{ color:black; text-align:left; font-size:16px; line-height:22px; font-weight:bold; margin:0; padding:5px 0 8px; }
		.su-bg .su-bkwh															{ background:#FFF none; } /*globals */
		.su-bg .su-bkbl															{ background:#000 none; }
		.su-bg .su-bkdk															{ background:#2B2B2B none; }
		.su-bg .su-grdn															{ background:#000 none; }
		.su-bg .su-grda															{ background:#03C2B2 none; }
		.su-bg .su-bkac															{ background:#03C2B2 none; }
		.su-bg .su-brda															{ border:1px solid #03C2B2; }
		.su-bg .su-brdd															{ border:1px solid #2B2B2B; }
		.su-bg #LeftPanel .su-bklt,
		.su-bg #su-main .su-bklt											{ background: white 0 0 repeat fixed; border: 1px red solid} /* text boxes */ /*TEXT BOX BACKGROUND */
/* 
		.su-bg #LeftPanel .su-brdm,
		.su-bg #su-main .su-brdm											{ border:1px solid #2A2A2A; } */
		/* .su-bg #RightPanel .su-brdm,
		.su-bg #su-main .su-brdm											{ border:0px solid red; } */
		/* no border content box */
		.su-bg .su-sbox, #su-deal, .su-bg .su-tbox,
		.su-bg #su-main-tabs .su-tbox									{ border-width:0 2px 2px !important; }
		.su-bg .su-pbox															{ border-width:2px !important; }
		.su-bg .su-sbox .su-tins, .su-bg .su-tbox .su-tins,
		.su-bg .su-pbox .su-tins											{ padding:10px 12px; } /* spacings */
		.su-bg .su-prom															{ margin:0 auto 15px; }
		#LeftPanel .su-ttba													{ padding:8px 12px; } /* title bars with bg */
		#RightPanel .su-ttba													{padding-bottom: 12px;} /* title bars with bg */
		#su-main .su-ttba														{ padding:8px 12px; }
		.su-bg .su-ffac, .su-bg .su-ffac p, .su-bg .su-ffac a { font-family:Exo, sans-serif; text-decoration:none; }
		.su-bg .su-fftb, .su-bg .su-fftb p, .su-bg .su-fftb a	{ color:black; font-size:22px; line-height:28px; font-weight:bold; font-style:italic; text-transform:uppercase; text-shadow:1px 1px #000; }
		.su-bg #su-main .su-fftb											{ text-align:center;}
		.su-bg #LeftPanel .su-bktt,
		.su-bg #su-main .su-bktt											{ background:white center top fixed repeat; border: red solid 3px; } /* THE TOP TEXT AREA BACKGROUND IS HERE! */
		.su-bg #RightPanel .su-bktt,
		.su-bg #su-main .su-bktt											{ background:transparent; border-bottom: 1px red solid; color:white;}
		.su-bg #su-main [type=radio] ~ label.su-bktt						{ background-image:url(images/nt-icon-plus.png); background-position:right 10px center; background-repeat:no-repeat; padding-right:28px !important; }
		.su-bg #su-main [type=radio]:checked ~ label.su-bktt	{ background-image:url(images/nt-icon-mins.png); }
		.su-bg #su-main [type=radio] ~ label.su-bktt						{ margin-bottom:1px; }
		.su-bg #su-main [type=radio]:checked ~ label.su-bktt	{ margin-bottom:0; }
		.su-bg #su-main [type=radio]:checked ~ label.su-bktt	{ background-color:#000; color:#03C2B2; border-color:#444; }
		.su-bg .su-ffbn, .su-bg a.su-ffbn								{ background:#03C2B2 none; } /* buttons */
		.su-bg .su-ffbn:hover, .su-bg a.su-ffbn:hover		{ background:#018F83 none; }
		.su-bg .su-brdb,
		.su-bg .su-brdb:hover												{ border:0 none; }
		.su-bg .su-ffbn, .su-bg a.su-ffbn								{ color:#000; font-size:13px; font-weight:bold; text-transform:uppercase; font-style:italic; height:30px; line-height:30px; padding:0 10px; display:block; }
		.su-bg .su-ffbn:hover, .su-bg a.su-ffbn:hover		{ color:#FFF; }
		.su-bg .su-ffbn.su-crnr, .su-bg a.su-ffbn.su-crnr,
		.su-bg .su-crnr, .su-bg .su-pbox								{ -moz-border-radius:5px; border-radius:5px; } /* rounding */
		.su-bg .su-ffbn.su-crns, .su-bg a.su-ffbn.su-crns,
		.su-bg .su-crns															{ -moz-border-radius:4px; border-radius:4px; } /* inset rounded corners */
		.su-bg #su-head-srch-bttn.su-ffbn.su-crns			{ -moz-border-radius:0 4px 4px 0; border-radius:0 4px 4px 0; } /* adjust header search box button */
		.su-bg .su-sbox, .su-bg .su-tbox								{ -moz-border-radius:0 0 5px 5px; border-radius:0 0 5px 5px; } /* text box corners */
		.su-bg .su-ttba															{ -moz-border-radius:5px 5px 0 0; border-radius:5px 5px 0 0; } /* title bar optional rounded edges */
		.su-bg .su-ttnc															{ -moz-border-radius:0; border-radius:0; } /* remove corners on accordion title bars */
		#su-main-tabs .su-tbox												{ -moz-border-radius:0px; border-radius:0px; } /* remove corners on accordion boxes */
		#su-main-tabs .su-tbox:last-child							{ -moz-border-radius:0 0 5px 5px; border-radius:0 0 5px 5px; } /* add corners back to bottom of accordion */
		.su-bg .su-prom.su-prot											{ -moz-border-radius:5px; border-radius:5px; } /* resizeable promo banners rounded corners */
		.su-bg #su-head-mnav .su-mbox [type=checkbox] ~ label						{ -moz-border-radius:5px; border-radius:5px; } /* header mobile dropdown menu */
		.su-bg #su-head-mnav .su-mbox [type=checkbox]:checked ~ label	{ -moz-border-radius:5px 5px 0 0; border-radius:5px 5px 0 0; } /* header mobile dropdown menu */
		.su-bg #su-head-mnav .su-mnav																{ -moz-border-radius:0 0 5px 5px; border-radius:0 0 5px 5px; } /* header mobile dropdown menu */
		/* ---------------------------------------- 
		eBay Header
		---------------------------------------- */
		.su-bg #su-head-wrap-01										{ background:white 0 0 repeat; border:1px solid #444; border-width:2px 0; }
		.su-bg #su-head-wrap-02										{ background:transparent;}
		.su-bg #su-head-wrap-03										{ background:black 0 0 repeat;}
		.su-bg #su-head-01													{ padding:5px 0; }
				
		.su-bg #su-head-logo												{ margin:15px auto; } /* logo */
		@media screen and (max-width:1020px)					{ .su-bg #su-head-logo { margin:15px auto 15px; } }
		.su-bg #su-head-srch												{ height:30px; position:relative; margin:0 auto; padding:0; float:right; } /* search box */
		.su-bg #su-head-srch-sbox										{ width:59%; height:30px; line-height:30px; padding:0 10px; float:left; }
		.su-bg #su-head-srch-bttn										{ float:right; }
		@media screen and (max-width:1440px)					{ .su-bg #su-head-srch { margin-right:10px; } }
		@media screen and (max-width:1020px)					{ .su-bg #su-head-srch { margin:10px auto; float:none; } }
		@media screen and (max-width:350px)					{ .su-bg #su-head-srch-bttn.su-ffbn { font-size:11px; line-height:16px; } }
		.su-bg #su-head-srch-sbox										{ color:#666; font-size:13px; }
		.su-bg #su-head-srch.su-bkwh,
		.su-bg #su-head-srch-sbox.su-bkwh						{ background-color:#FFF; }
		/* no border */
		.su-bg .su-brds															{ border:0 none; }
		.su-bg #su-head-srch-sbox										{ border-width:0; }
		.su-bg #su-head-srch-bttn										{ border-width:0; }
		.su-bg #su-head-tnav												{ height:18px; padding:5px 0; } /* top nav menu */
		@media screen and (max-width:1020px)					{ .su-bg #su-head-tnav { display:none; } }
		.su-bg #su-head-tnav a											{ color:#FFF; font:normal 13px/20px "Ropa Sans", sans-serif; font-style:italic; text-transform:uppercase; display:inline-block; padding:0 15px; }
		.su-bg #su-head-tnav a:hover								{ color:#03C2B2;  text-decoration:none; }
		.su-bg #su-head-tnav a:first-child							{ padding-left:0; }
		.su-bg #su-head-tnav a:last-child							{ padding-right:0; }
		/* add divider icons */
		.su-bg #su-head-tnav a:before								{ content:url(images/nt-icon-lev1h.png); vertical-align:middle; height:20px; line-height:20px; padding-right:5px; }
		/* left align */
		.su-bg #su-head-tnav												{ float:left; text-align:left; }
		#su-template.su-bg #su-head-tnav							{ float:none; text-align:center; margin:0 auto; }
		@media screen and (max-width:1440px)					{ .su-bg #su-head-tnav { margin-left:10px; } #su-template.su-bg #su-head-tnav { margin-left:auto; } }
		.su-bg #su-head-mnav												{ height:auto; position:relative; clear:both; margin:0 auto 15px; } /* mobile dropdown menu */
		#su-template.su-bg #su-head-mnav						{ margin:0 auto; }
		.su-bg #su-head-mnav .su-mbox label						{ width:100%; position:relative; left:0; display:block; cursor:pointer; text-align:left; margin:0 auto; padding:0 8px; }
		.su-bg #su-head-mnav .su-mbox [type=checkbox]	{ display:none; }
		.su-bg #su-head-mnav .su-mbox [type=checkbox] ~ label										{ background-image:url(images/nt-icon-open.png); background-position:right 6px center; background-repeat:no-repeat; padding-right:30px !important; }
		.su-bg #su-head-mnav .su-mbox [type=checkbox]:checked ~ label					{ background-image:url(images/nt-icon-shut.png); z-index:2; } /* tab hover effect */
		.su-bg #su-head-mnav .su-mbox [type=checkbox] ~ label ~ .su-mnav					{ display:none; }
		.su-bg #su-head-mnav .su-mbox [type=checkbox]:checked ~ label ~ .su-mnav	{ display:block; z-index:1; }
		.su-bg #su-head-mnav .su-mnav								{ margin:0; max-height:600px; padding:4px 0px; overflow:auto; top:0; left:0; right:0; bottom:0; position:relative; text-align:left; width:100%; max-width:300px; }
		.su-bg #su-head-mnav .su-mnav ul							{ list-style:none; margin:0; padding:0; }
		.su-bg #su-head-mnav .su-mnav ul li						{ display:block; margin:0; padding:0 8px; }
		.su-bg #su-head-mnav												{ display:none; }
		@media screen and (max-width:1020px)					{ .su-bg #su-head-mnav { display:block; } }
		/* background colors */
		.su-bg #su-head-mnav .su-mbox label,
		.su-bg #su-head-mnav .su-mnav								{ background-color:#FFF; }
		/* font styling */
		.su-bg #su-head-mnav .su-mbox label						{ color:#353535; font:normal 14px/30px "Ropa Sans", sans-serif; }
		.su-bg #su-head-mnav .su-mnav h4							{ color:#03C2B2; font:bold 14px/30px "Ropa Sans", sans-serif; padding:0 8px }
		.su-bg #su-head-mnav .su-mnav ul li a					{ color:#353535; font:normal 13px/22px "Ropa Sans", sans-serif; text-decoration:none; display:block; }
		.su-bg #su-head-mnav .su-mnav ul li a:hover		{ color:#03C2B2; text-decoration:none; }
		/* add icons */
		.su-bg #su-head-mnav .su-mnav ul li a					{ background-image:url(images/nt-icon-lev1.png); background-position:0px 5px; background-repeat:no-repeat; padding-left:14px; }
		.su-bg #su-head-mnav .su-mnav ul li a:hover		{ background-image:url(images/nt-icon-lev1h.png); }
		.su-bg #su-head-whys												{ width:100%; text-align:center; padding-top:10px;} /* why shop bar */
		.su-bg #su-head-whys img										{ width:auto; max-width:300px; display:inline-block; margin:0 70px 10px; }
		.su-bg #su-head-whys img:first-child					{ margin-left:0; }
		.su-bg #su-head-whys img:nth-child(4)				{ margin-right:0; }
		.su-bg #su-head-whys img#su-head-whys-all		{ display:none; }
		@media screen and (max-width:1440px)					{ .su-bg #su-head-whys img { margin:0 60px 10px; } }
		@media screen and (max-width:1250px)					{ .su-bg #su-head-whys img { margin:0 50px 10px; } }
		@media screen and (max-width:1160px)					{ .su-bg #su-head-whys img { margin:0 40px 10px; } }
		@media screen and (max-width:1090px)					{ .su-bg #su-head-whys img { margin:0 30px 10px; } }
		@media screen and (max-width:1000px)					{ .su-bg #su-head-whys img { margin:0 20px 10px; } }
		@media screen and (max-width:950px)					{ .su-bg #su-head-whys img { display:none; } .su-bg #su-head-whys img#su-head-whys-all { display:block; margin:0 auto 10px; } }
		/* ---------------------------------------- 
		eBay Left Panel
		---------------------------------------- */
		.su-bg #LeftPanel .lev1 li a,
		/* .su-bg #su-side-cats ul li a										{ color:#FFF; } categories nav */
		.su-bg #LeftPanel .lev1 li a:hover,
		.su-bg #su-side-cats ul li a:hover,
		.su-bg #LeftPanel .lev1 li span									{ color:#03C2B2; }
		.su-bg #LeftPanel #su-side-cats .su-tins				{ padding:0; }
		.su-bg #LeftPanel .lev1 li a, 
		.su-bg #LeftPanel .lev1 li span									{ font-size:16px; line-height:19px; font-weight:normal; }
		.su-bg #LeftPanel .lev2 li a,
		.su-bg #LeftPanel .lev2 li span	       							{ font-size:14px; line-height:16px; font-weight:normal; }
		.su-bg #LeftPanel .lev3 li a,
		.su-bg #LeftPanel .lev3 li span	       							{ font-size:14px; line-height:16px; font-weight:normal; }
		.su-bg #LeftPanel .lev2,
		.su-bg #LeftPanel .lev3												{ padding-bottom:5px; }
		/* add dividers */
		.su-bg #LeftPanel .lev1 li											{ border:1px solid #3A3A3A; border-width:1px 0 0; }
		.su-bg #LeftPanel .lev1 li:first-child,
		.su-bg #LeftPanel .lev2 li,
		.su-bg #LeftPanel .lev3 li											{ border-width:0; }
		/* add bullets / icons */
		.su-bg #LeftPanel .lev1 li a,
		.su-bg #LeftPanel .lev1 li span				        			{ background:transparent url(images/nt-icon-lev1.png) 10px 10px no-repeat; padding:7px 10px 7px 24px; }
		.su-bg #LeftPanel .lev1 li a:hover,
		.su-bg #LeftPanel .lev1 li span				            		{ background-image:url(images/nt-icon-lev1h.png); }
		.su-bg #LeftPanel .lev2 li a,
		.su-bg #LeftPanel .lev2 li span			        				{ background:transparent url(images/nt-icon-lev2.png) 23px 7px no-repeat; padding:5px 10px 5px 36px; }
		.su-bg #LeftPanel .lev3 li a,
		.su-bg #LeftPanel .lev3 li span				        			{ background:transparent url(images/nt-icon-lev2.png) 35px 7px no-repeat; padding:5px 10px 5px 48px; }
		.su-bg #LeftPanel .lev2 li a:hover,
		.su-bg #LeftPanel .lev3 li a:hover,
		.su-bg #LeftPanel .lev2 li span,
		.su-bg #LeftPanel .lev3 li span			            			{ background-image:url(images/nt-icon-lev2h.png); }
		#su-side-news p														{ line-height:18px; margin:0 0 10px; } /* newsletter box */
		#su-side-news-bttn													{ float:right; }
		#su-side-news-bttn													{ color:#FFF; background-color:#03C2B2; border-color:#03C2B2; }
		#su-side-news-bttn:hover										{ color:#FFF; background-color:#353535; border-color:#353535; }
		.su-bg #LeftPanel .su-prot										{ background:white url(images/nt-side-prom.jpg) 0 0 repeat; border:1px solid #3A3A3A; border-width:2px; } /* text promo banners */
		.su-bg #LeftPanel .su-prot .su-tins							{ padding:10px 10px; text-align:right; }
		.su-bg #LeftPanel .su-prot .su-icon							{ display:block; margin-right:15px; float:right; width:60px; height:60px; }
		.su-bg #LeftPanel .su-prot span								{ color:#03C2B2; font:normal 23px/26px Exo, sans-serif; text-transform:uppercase; font-style:italic; text-shadow:1px 1px #000; display:block; float:right; padding-top:4px; }
		.su-bg #LeftPanel .su-prot span span						{ color:#FFF; float: right; padding-top:0; font-size:15px; }
		@media screen and (max-width:1250px)					{ .su-bg #LeftPanel .su-prot span { font-size:20px; line-height:23px; padding-top:2px; } .su-bg #LeftPanel .su-prot .su-icon { width:50px; height:50px; margin-right:10px; } }
		@media screen and (max-width:1130px)					{ .su-bg #LeftPanel .su-prot span { float:right; text-align:center; padding-top:0; }  .su-bg #LeftPanel .su-prot .su-icon { float:right; margin:0 auto 5px; } }
		/* ---------------------------------------- 
		eBay Right Panel
		---------------------------------------- */
		.su-bg #RightPanel .lev1 li a,
		/* .su-bg #su-side-cats ul li a										{ color:#FFF; } categories nav */
		.su-bg #RightPanel .lev1 li a:hover,
		.su-bg #su-side-cats ul li a:hover,
		.su-bg #RightPanel .lev1 li span									{ color:black; }
		.su-bg #RightPanel #su-side-cats .su-tins				{ padding:0; }
		.su-bg #RightPanel .lev1 li a, 
		.su-bg #RightPanel .lev1 li span									{ font-size:16px; line-height:19px; font-weight:normal; }
		.su-bg #RightPanel .lev2 li a,
		.su-bg #RightPanel .lev2 li span	       							{ font-size:14px; line-height:16px; font-weight:normal; }
		.su-bg #RightPanel .lev3 li a,
		.su-bg #RightPanel .lev3 li span	       							{ font-size:14px; line-height:16px; font-weight:normal; }
		.su-bg #RightPanel .lev2,
		.su-bg #RightPanel .lev3												{ padding-bottom:5px; }
		/* add dividers */
		.su-bg #RightPanel .lev1 li											{ border-width:1px 0 0; }
		.su-bg #RightPanel .lev1 li:first-child,
		.su-bg #RightPanel .lev2 li,
		.su-bg #RightPanel .lev3 li											{ border-width:0; }
		/* add bullets / icons */
		.su-bg #RightPanel .lev1 li a,
		.su-bg #RightPanel .lev1 li span				        			{ background:transparent 10px 10px no-repeat; text-decoration: none; }
		.su-bg #RightPanel .lev1 li a:hover,
		.su-bg #RightPanel .lev1 li span				            		{ background-image:url(images/nt-icon-lev1h.png); }
		.su-bg #RightPanel .lev2 li a,
		.su-bg #RightPanel .lev2 li span			        				{ background:transparent url(images/nt-icon-lev2.png) 23px 7px no-repeat; padding:5px 10px 5px 36px; }
		.su-bg #RightPanel .lev3 li a,
		.su-bg #RightPanel .lev3 li span				        			{ background:transparent url(images/nt-icon-lev2.png) 35px 7px no-repeat; padding:5px 10px 5px 48px; }
		.su-bg #RightPanel .lev2 li a:hover,
		.su-bg #RightPanel .lev3 li a:hover,
		.su-bg #RightPanel .lev2 li span,
		.su-bg #RightPanel .lev3 li span			            			{ background-image:url(images/nt-icon-lev2h.png); }
		#su-side-news p														{ line-height:18px; margin:0 0 10px; } /* newsletter box */
		#su-side-news-bttn													{ float:right; }
		#su-side-news-bttn													{ color:#FFF; background-color:#03C2B2; border-color:#03C2B2; }
		#su-side-news-bttn:hover										{ color:#FFF; background-color:#353535; border-color:#353535; }
		.su-bg #RightPanel .su-prot										{ background:white url(images/nt-side-prom.jpg) 0 0 repeat; border:1px solid #3A3A3A; border-width:2px; } /* text promo banners */
		.su-bg #RightPanel .su-prot .su-tins							{ padding:10px 10px; text-align:right; }
		.su-bg #RightPanel .su-prot .su-icon							{ display:block; margin-right:15px; float:right; width:60px; height:60px; }
		.su-bg #RightPanel .su-prot span								{ color:#03C2B2; font:normal 23px/26px Exo, sans-serif; text-transform:uppercase; font-style:italic; text-shadow:1px 1px #000; display:block; float:right; padding-top:4px; }
		.su-bg #RightPanel .su-prot span span						{ color:#FFF; float: right; padding-top:0; font-size:15px; }
		@media screen and (max-width:1250px)					{ .su-bg #RightPanel .su-prot span { font-size:20px; line-height:23px; padding-top:2px; } .su-bg #RightPanel .su-prot .su-icon { width:50px; height:50px; margin-right:10px; } }
		@media screen and (max-width:1130px)					{ .su-bg #RightPanel .su-prot span { float:right; text-align:center; padding-top:0; }  .su-bg #RightPanel .su-prot .su-icon { float:right; margin:0 auto 5px; } }
		/* ---------------------------------------- 
		eBay Homepage
		---------------------------------------- */
		#su-main-babg															{ width:100%; height:auto; background:transparent none; margin:15px auto 0; padding:0; display:none; } /* welcome banner extended */
		#su-main-babg #su-main-bann								{ width:100%; max-width:1400px; height:auto; margin:0 auto; display:block; text-align:center; -moz-border-radius:5px; border-radius:5px; border:2px solid #03C2B2; }
		#su-main-babg .su-pmob											{ display:none !important; }
		@media screen and (max-width:700px) 					{ #su-main-babg .su-pmob { display:block !important; } }
		#su-main-fcat															{ width:100%; text-align:center; background:transparent none; display:none; } /* featured category banners expanded */
		#su-main-fcat .su-tins												{ width:100%; max-width:1400px; margin:0 auto; padding:0; text-align:center; overflow:hidden; }
		/* for 4 across */
		#su-main-fcat a															{ width:335px; max-width:335px; height:auto; border:2px solid #444; -moz-border-radius:5px; border-radius:5px; margin:15px 0 0 20px; float:left; }
		#su-main-fcat a.su-first											{ margin-left:0; }
		#su-main-fcat a img													{ width:100%; height:auto; }
		@media screen and (max-width:1440px)					{  #su-main-fcat a, #su-main-fcat a.su-first { width:23%; height:auto; display:inline-block; float:none; margin:15px 10px 0; } }
		@media screen and (max-width:1140px)					{  #su-main-fcat a, #su-main-fcat a.su-first { margin:15px 7px 0; } }
		@media screen and (max-width:950px)					{ #su-main-fcat a, #su-main-fcat a.su-first { width:47%; } }
		@media screen and (max-width:540px)					{ #su-main-fcat a, #su-main-fcat a.su-first { width:100%; margin:15px auto 0; } }
		@media screen and (max-width:350px)					{ #su-main-fcat a, #su-main-fcat a.su-first { width:95%; } }
		#su-main-feat #su-feat .su-fp									{ width:174px; height:313px; padding-top:7px; background:transparent url(images/nt-main-fbox.png) center top no-repeat; } /* featured products */
		#su-main-feat #su-feat .su-fp a,
		#su-main-feat #su-feat .su-fp a span						{ text-align:left; font-size:14px; line-height:17px; display:block; }
		#su-main-feat #su-feat .su-fp a .title						{ color:#C5D5D4; height:68px; margin:4px 8px 4px; text-align:center; }
		#su-main-feat #su-feat .su-fp a:hover .title			{ color:#FFF; }
		#su-main-feat #su-feat .su-fp a .price					{ color:#03C2B2; font:bold 18px/30px "Ropa Sans", sans-serif; height:30px; display:block; padding:0 12px 50px; text-align:center; }
		#su-main-feat #su-feat .su-fp a .thumb					{ width:174px; height:160px; display:table-cell; vertical-align:middle; text-align:center; }
		#su-main-feat #su-feat .su-fp a .thumb img			{ max-height:140px; width:auto; max-width:140px; margin:10px auto; }
		/* centered 5 across */
		#su-main-feat															{ padding:0 0 20px; text-align:center; }
		#su-main-feat #su-feat												{ display:inline-block; }
		#su-main-feat #su-feat .su-fp									{ margin:20px 17px 0; display:inline-block; }
		@media screen and (max-width:460px)					{ #su-main-feat #su-feat .su-fp { margin:20px 5px 0; } }
		@media screen and (max-width:430px)					{ #su-main-feat #su-feat .su-fp { margin:15px 2px 0; } #su-main-feat #su-feat .su-fp, #su-main-feat #su-feat .su-fp a .thumb { width:164px; } }
		@media screen and (max-width:400px)					{ #su-main-feat #su-feat .su-fp, #su-main-feat #su-feat .su-fp a .thumb { width:148px; } }
		/* add hover */
		#su-main-feat #su-feat .su-fp:hover						{ background-image:url(images/nt-main-fboxh.png); }
		/* adust for mobile */
		@media screen and (max-width:410px)					{ #su-main-feat #su-feat .su-fp { width:142px; } #su-main-feat #su-feat .su-fp:hover { } }
		@media screen and (max-width:350px) {
		#su-main #su-main-feat #su-feat .su-fp:nth-child(1),
		#su-main #su-main-feat #su-feat .su-fp:nth-child(3),
		#su-main #su-main-feat #su-feat .su-fp:nth-child(5),
		#su-main #su-main-feat #su-feat .su-fp:nth-child(7),
		#su-main #su-main-feat #su-feat .su-fp:nth-child(9),
		#su-main #su-main-feat #su-feat .su-fp:nth-child(11)	{ margin-left:0; }
		#su-main #su-main-feat #su-feat .su-fp:nth-child(2),
		#su-main #su-main-feat #su-feat .su-fp:nth-child(4),
		#su-main #su-main-feat #su-feat .su-fp:nth-child(6),
		#su-main #su-main-feat #su-feat .su-fp:nth-child(8),
		#su-main #su-main-feat #su-feat .su-fp:nth-child(10),
		#su-main #su-main-feat #su-feat .su-fp:nth-child(12)	{ margin-right:0; }
		}
		@media screen and (max-width:339px)					{ #su-main-feat #su-feat .su-fp { width:174px; margin:15px auto 0 !important; } #su-main-feat #su-feat .su-fp:hover { } }
		/* ---------------------------------------- 
		eBay Listing Template
		---------------------------------------- */
		#su-template.su-bg #su-main-gall h1						{ text-transform:uppercase; font-style:italic; border:1px solid #444; border-width:0 0 1px; padding:8px 0; margin-bottom:5px; text-decoration: none;}
		#su-template #su-main-desc h5								{ display:none; }
		.su-bg #su-main #su-gall-right									{ background-color:transparent; text-align: left;font-size: 17px; }
		#su-temp-gall.su-bttm #su-gall-main						{ border:1px solid #444; background-color:#111; } /* product photo gallery */
		#su-temp-gall #su-gall-thmb h5								{ font-size:15px !important; text-transform:uppercase; font-style:italic; color:black; }
		#su-temp-gall.su-bttm #su-gall-thmb .su-hold						{ border:1px solid red; background-color:#111; }
		#su-temp-gall.su-bttm #su-gall-thmb .su-hold:hover			{ border:1px solid red; }
		#su-temp-gall #su-gall-thmb h5 span						{ background-image:url(images/nt-icon-gall.png) }
		#su-temp-gall.su-bttm .su-cntr								{ background-color:transparent; }
		.su-bg #su-main-shop												{ border:0 none; background:transparent url(images/nt-main-prom.jpg) right center no-repeat; -moz-border-radius:5px; border-radius:5px; border:2px solid #03C2B2; } /* shop our store promo banner */
		.su-bg #su-main-shop .su-tins									{ padding:15px 15px; }
		.su-bg #su-main-shop .su-left									{ color:#FFF; font:normal 28px/40px "Ropa Sans", sans-serif; font-style:italic; text-transform:uppercase; display:inline-block; text-align:right; float:left; text-shadow:0 0 10px rgba(0, 0, 0, 0.8); }
		.su-bg #su-main-shop .su-left .su-font					{ color:#FFF; font-size:32px; font-family:Exo, sans-serif; font-weight:normal; }
		.su-bg #su-main-shop a											{ display:inline-block; height:auto; line-height:18px; padding:8px 15px; margin-top:13px; margin-left:40px; float:left; }
		@media screen and (max-width:1080px)					{ .su-bg #su-main-shop { background-position:left center; } .su-bg #su-main-shop .su-left { display:block; margin:0 auto 10px; float:none; } .su-bg #su-main-shop a { display:inline-block; margin:0 auto; float:none; } }
		@media screen and (max-width:420px)					{ .su-bg #su-main-shop .su-left { font-size:24px; line-height:32px; } .su-bg #su-main-shop .su-left .su-font { font-size:28px; line-height:32px; } }
		.su-bg #su-main #su-main-tabs								{  } /* terms of sale accordion */
		.su-ttrm																		{ background:#000 none; }
		/* ---------------------------------------- 
		eBay Footer Extended
		---------------------------------------- */
		#su-foot-wrap															{ background:white 0 0 repeat; /* border:1px solid #03C2B2; border-width:2px 0 0;*/ } /* general */
		#su-foot-main															{ background:transparent none; }
		#su-foot-main .su-foot-tins										{ background:transparent none; width:100%; max-width:1400px; height:auto; margin:0 auto; padding:0; }
		#su-foot-main .su-foot-cols										{ width:25%; height:60px; float:left; padding:20px 25px; /* border-right:1px solid white*/; border-bottom:1px solid #333;}
		#su-foot-main #su-foot-col4.su-foot-cols				{ border-right:0 none; }
		/* #su-foot-main #su-foot-col1.su-foot-cols				{ width:20%;} */
		/* #su-foot-main #su-foot-col2.su-foot-cols				{ width:20% }
		#su-foot-main #su-foot-col3.su-foot-cols				{ width:25%; }
		#su-foot-main #su-foot-col4.su-foot-cols				{ width:35%; } */
		@media screen and (max-width:1150px) {
		#su-foot-main #su-foot-col4.su-foot-cols 				{ display:none; }
		#su-foot-main #su-foot-col1.su-foot-cols,
		#su-foot-main #su-foot-col2.su-foot-cols,
		#su-foot-main #su-foot-col3.su-foot-cols				{ width:33%; }
		#su-foot-main #su-foot-col3.su-foot-cols				{ border-right:0 none; }
		}
		@media screen and (max-width:800px) {
		#su-foot-main #su-foot-col1.su-foot-cols,
		#su-foot-main #su-foot-col2.su-foot-cols				{ width:100%; height:auto; float:none; border-right:0 none; }
		#su-foot-main #su-foot-col3.su-foot-cols				{ width:100%; height:auto; float:none; }
		}
		#su-foot-main .su-foot-cols h3									{ /*color:#03C2B2;*/ font:bold 16px/19px Exo, sans-serif; font-style:italic; margin:0 0 20px; padding:0; clear:both; }
		#su-foot-main .su-foot-cols ul									{ list-style-type:none; margin:0; padding:0; }
		#su-foot-main .su-foot-cols ul li								{ background:transparent 0 3px no-repeat; padding:0 0 10px 16px; }
		#su-foot-main .su-foot-cols #su-foot-menu ul li:hover { background-image:url(images/nt-icon-lev1h.png); }
		#su-foot-main .su-foot-cols ul li,
		#su-foot-main .su-foot-cols ul li a,
		#su-foot-main .su-foot-cols p									{ color:#FFF; font-size:14px; line-height:18px; }
		#su-foot-main .su-foot-cols #su-foot-menu ul li:hover a	{ color:#03C2B2; text-decoration:none; }
		#su-foot-main .su-foot-cols #su-foot-mail p			{ color:#FFF; margin:0 0 5px; padding:0; }
		#su-foot-main .su-foot-cols #su-foot-mail a			{ float:right; }
		#su-foot-main .su-foot-cols #su-foot-mail a.su-brdb.su-crnr.su-ffac.su-ffbn 				{ /* color:#FFF; background:#03C2B2 none; border:0 none; */ }
		#su-foot-main .su-foot-cols #su-foot-mail a.su-brdb.su-crnr.su-ffac.su-ffbn:hover 	{ /* color:#FFF; background:#353535 none; border:0 none; */ }
		#su-foot-main .su-foot-cols #su-foot-mssg p			{ color:#FFF; margin:0 0 5px; padding:0; }
		#su-foot-main .su-foot-cols #su-foot-mssg a			{ float:right; }
		#su-foot-main .su-foot-cols #su-foot-mssg a.su-brdb.su-crnr.su-ffac.su-ffbn 				{ /* color:#FFF; background:#03C2B2 none; border:0 none; */ }
		#su-foot-main .su-foot-cols #su-foot-mssg a.su-brdb.su-crnr.su-ffac.su-ffbn:hover 	{ /* color:#FFF; background:#353535 none; border:0 none; */ }
		#su-foot-main .su-foot-cols #su-foot-icon				{ text-align:center; }
		#su-foot-main .su-foot-cols #su-foot-icon img		{ display:inline-block; margin:0 10px 20px; max-width:100%; vertical-align:middle; }
		#su-foot-main .su-foot-cols #su-foot-icon img:nth-child(1),
		#su-foot-main .su-foot-cols #su-foot-icon img:nth-child(2)	{ display:block; margin:0 auto 20px; }
		@media screen and (max-width:800px) { /* center footer content on mobile */
		#su-foot-main .su-foot-cols h3,
		#su-foot-main .su-foot-cols ul li,
		#su-foot-main .su-foot-cols p,
		#su-foot-main .su-foot-cols #su-foot-mail,
		#su-foot-main .su-foot-cols #su-foot-mssg,
		#su-foot-main .su-foot-cols #su-foot-cont				{ text-align:center; }
		#su-foot-main .su-foot-cols h3									{ margin-bottom:10px; }
		#su-foot-main .su-foot-cols #su-foot-mssg h3,
		#su-foot-main .su-foot-cols #su-foot-cont h3		{ margin-top:15px; }
		#su-foot-main .su-foot-cols #su-foot-mail p,
		#su-foot-main .su-foot-cols #su-foot-mssg p,
		#su-foot-main .su-foot-cols #su-foot-cont p			{ margin-bottom:20px; }
		#su-foot-main .su-foot-cols a.su-ffbn						{ float:none !important; display:inline-block; margin:0 auto; }
		#su-foot-main .su-foot-cols ul li,
		#su-foot-main .su-foot-cols ul li:hover					{ background-image:none; padding-left:0; }
		}
		#su-foot-copy							    							{ width:100%; height:auto; padding:0; text-align:center; clear:all; }
		#su-foot-copy p														{ margin:0; padding:20px 25px; height:15px; } /* copyright line */
		#su-foot-copy p, #su-foot-copy a							{ color:#FFF; font-size:13px; line-height:16px; }
		#su-foot-copy a:first-child										{ }
		#su-foot-copy a:hover							    			{ color:#FFF; text-decoration:underline; }
		#su-foot-copy .su-copy-ninja,
		#su-foot-copy .su-copy-ninja2								{ margin-left:10px; padding-left:10px; border-left:1px solid #FFF; display:inline-block; }
		@media screen and (max-width:630px) 					{ #su-foot-copy p { height:auto; } #su-foot-copy, #su-foot-copy * { line-height:1.2; } #su-foot-copy .su-copy-ninja, #su-foot-copy .su-copy-ninja2 { display:block; margin-top:15px; margin-left:0; padding-left:0; border-left:0 none; } }
		/* ---------------------------------------- 
		eBay Category Page
		---------------------------------------- */
		.su-bg .v4stabl, .su-bg .v4stabl a								{ color:#BBB; } /* top right view links */
		.su-bg .v4stabl a:hover											{ color:#BBB;}
		.su-bg .r3_cm.bp.tp													{ border-top:1px solid #444; } /* top navigation box */
		.su-bg .ctrlbr																{ border-bottom:1px solid #444; }
		.su-bg .fpcc .countClass,
		.su-bg .fpcc .matchClass,
		.su-bg .fpcc .keywordClass										{ color:#BBB; font-family:"Ropa Sans", sans-serif; } /* top results count */
		.su-bg .fpcc .countClass											{ color:#03C2B2; }
		.su-bg td#CentralArea span.pdmt span.label			{ color:#BBB; } /* top view sort */
		.su-bg td#CentralArea span.pdmt span.cur			{ color:#BBB; }
		.su-bg .cmpBr .cmsg, .su-bg .cmpBr .cmsg a			{ color:#BBB; } /* top shipping to */
		.su-bg .cmpBr .cmsg a:hover									{ color:#03C2B2; }
		#su-main-cate .su-fp												{ height:350px; border:1px solid #444; } /* gallery box */
		#su-main-cate .su-fp a .title									{ color:#353535; }
		#su-main-cate .su-fp a:hover .title						{ color:#03C2B2; }
		#su-main-cate .su-fp .subtitle									{ color:#999; }
		#su-main-cate .su-fp .price-bin,
		#su-main-cate .su-fp .bid-price								{ color:#03C2B2; }
		#su-main-cate .su-fp .time-left								{ color:#999; }
		#su-main-cate .su-fp .shipping								{ color:#444; }
		.su-bg table.pgbc														{ border-top:1px solid #444; border-bottom:1px solid #444; padding:5px 0; } /* pagination lines */
		.su-bg .dynpg span.page,
		.su-bg .dynpg .r .form label										{ color:#BBB; } /* pagination text */
		.su-bg .dynpg .prev a.enabled,
		.su-bg .dynpg .prev a.enabled:hover,
		.su-bg .dynpg .next a.enabled,
		.su-bg .dynpg .next a.enabled:hover,
		.su-bg .dynpg td.pages a.enabled,
		.su-bg .dynpg td.pages a.enabled:visited				{ color:#BBB; }
		.su-bg .dynpg td.pages a.enabled:hover				{ color:#03C2B2; text-decoration:none; }
		.su-bg .dynpg .prev a.disabled,
		.su-bg .dynpg .prev a.disabled:hover,
		.su-bg .dynpg .next a.disabled,
		.su-bg .dynpg .next a.disabled:hover,
		.su-bg .dynpg td.pages a.disabled,
		.su-bg .dynpg td.pages a.disabled:hover,
		.su-bg .dynpg td.pages a.disabled:visited,
		.su-bg .dynpg span.pipe											{ color:#888; text-decoration:none; }
		.su-bg td#CentralArea span.pdmt span.cur			{ background-image:url(images/nt-cate-drop.png); } /* buttons and icons */
		#su-main-cate .su-fp .button									{ background-image:url(images/nt-cate-bttn.png); transition:all 0.5s ease; }
		#su-main-cate .su-fp:hover .button						{ background-image:url(images/nt-cate-bttnh.png); }
		.su-bg .dynpg .prev a												{ background-image:url(images/nt-cate-back.png) !important; }
		.su-bg .dynpg .next a												{ background-image:url(images/nt-cate-next.png) !important; }
		.su-bg .dynpg .r .form input#q_10							{ background-image:url(images/nt-cate-btgo.png) !important; }
		.su-bg .bpmsg																{ margin-top:10px; } /* search results page no results */
		.su-bg .bpmsg .title, .su-bg .bpmsg .option,
		.su-bg .bpmsg .lnk, .su-bg .bpmsg .lnk a					{ font-family:"Ropa Sans", sans-serif; font-size:13px; line-height:18px; }
		.su-bg .bpmsg .title													{ color:#BBB;  }
		.su-bg .bpmsg .option												{ color:#03C2B2; font-weight:normal; }
		.su-bg .bpmsg .lnk a													{ color:#03C2B2; font-weight:normal; margin-left:10px; padding-left:15px; background:transparent url(images/nt-icon-lev1h.png) 0 3px no-repeat; }
		.su-bg .v4snexp div													{ color:#999; margin-top:10px; }
		.su-bg .toplne .msg													{ color:#BBB; }
		.su-bg .toplne .msg b													{ color:#03C2B2; margin-left:4px; }
		.su-bg .toplne .msg span											{ margin-right:7px; }
		.su-bg .v4snexp ul li													{ color:#BBB; background:transparent url(images/nt-icon-lev1h.png) 0 3px no-repeat; }
		.su-bg .v4snexp ul li a												{ color:#03C2B2; }
		.su-bg .sifExp .expHeader											{ margin-bottom:15px; } /* search results page with additional items */
		.su-bg .sifExp .expHeader span								{ color:#999; font-weight:normal; }
		.su-bg .sifExp .expHeader span .ctgcnt					{ color:#03C2B2; font-weight:bold; }
		.su-bg .sifExp .expHeader b										{ color:#999; font-weight:bold; }
		.su-bg .sifExp .lview table tr										{ background-color:#FFF; border-bottom:1px solid #444; }
		.su-bg .sifExp .lview table tr td								{ vertical-align:middle; }
		.su-bg .sifExp .lview table tr td.pic							{ padding-left:10px; padding-right:10px; }
		* {box-sizing:border-box}
		/* Slideshow container */
		.slideshow-container {
		max-width: 200px;
		position: relative;
		margin: auto;
		}
		/* Hide the images by default */
		.mySlides {
		display: none;
		}
		/* Next & previous buttons */
		.prev, .next {
		cursor: pointer;
		position: absolute;
		top: 50%;
		width: auto;
		margin-top: -22px;
		padding: 16px;
		color: white;
		font-weight: bold;
		font-size: 18px;
		transition: 0.6s ease;
		border-radius: 0 3px 3px 0;
		user-select: none;
		}
		/* Position the "next button" to the right */
		.next {
		right: 0;
		border-radius: 3px 0 0 3px;
		}
		/* On hover, add a black background color with a little bit see-through */
		.prev:hover, .next:hover {
		background-color: rgba(0,0,0,0.8);
		}
		/* Caption text */
		/* .text {
		color: #f2f2f2;
		font-size: 15px;
		padding: 8px 12px;
		position: absolute;
		bottom: 8px;
		width: 100%;
		text-align: center;
		} */
		/* Number text (1/3 etc) */
		.numbertext {
		color: #f2f2f2;
		font-size: 12px;
		padding: 8px 12px;
		position: absolute;
		top: 0;
		}
		/* The dots/bullets/indicators */
		.dot {
		cursor: pointer;
		height: 15px;
		width: 15px;
		margin: 0 2px;
		background-color: #bbb;
		border-radius: 50%;
		display: inline-block;
		transition: background-color 0.6s ease;
		}
		.active, .dot:hover {
		background-color: #717171;
		}
		/* Fading animation */
		.fade {
		-webkit-animation-name: fade;
		-webkit-animation-duration: 1.5s;
		animation-name: fade;
		animation-duration: 1.5s;
		}
		@-webkit-keyframes fade {
		from {opacity: .4}
		to {opacity: 1}
		}
		@keyframes fade {
		from {opacity: .4}
		to {opacity: 1}
		}
		.product_carasel {
		background-color: transparent;
		/* margin-top: 30px; */
		margin-bottom: 30px;
		}
		.product_carasel .content{
		height: auto;
		width: auto;
		display: flex;
		justify-content: space-evenly;
		}
		.product_carasel img {
		float: left;
		/* height: 300px; */
		/* height: 20vw; */
		height: 300px;
		max-width: 100%;
		padding: 10px 10px 10px 10px;
		border-radius: 50px;
		}
		.product_carasel #section1 {
		/* max-width: 100px; */
		background-color: transparent;
		}
		.product_carasel #section2 {
		background-color: transparent;
		}
		.product_carasel #section3 {
		background-color: transparent;
		}
		.product_carasel .controls #button1 {
		padding: 32px 32px;
		height: 300px;
		border-radius: 12px;
		color: grey;
		/* background: black; */
		/* background-size: 300%; */
		background-color: transparent;
		border: none;
		float: left;
		/* width: 100px; */
		outline: none;
		cursor: pointer;
		}
		.product_carasel .controls #button2 {
		padding: 32px 32px;
		height: 300px;
		border-radius: 12px;
		color: grey;
		/* background: black; */
		/* background-size: 300%; */
		background-color: transparent;
		border: none;
		float: right;
		width: 100px;
		outline: none;
		cursor: pointer;
		}
		.spacer {
		height: 1100px;
		}
		.infomenu {
			width:140px;
			background-color: black;
			padding-top: 30px;
			padding-bottom: 30px;
			margin: 0 auto;
		}
		.infomenu .contents {
			width: 100%;
		}
		.infomenu .contents .text {
			margin: 0 auto;
			color: white;
			font-size: 30px;
			margin-top: 10px;
		}
		.infomenu .contents .text:hover {
			margin-top: 9px;
			border-bottom: red 1px solid;
		}
		.contactus {
		height: 600px;
		width: 100%;
		/* transform: translate(34%); */
		margin-bottom: 20px;
		padding-top:20px;
		}
		.contactus .bannerimage{
		/* padding-top: 30px; */
		height: 300px;
		width: 100%;
		background-image: url("banner 1.png");
		background-attachment: fixed;
		background-position: center;
		background-repeat: no-repeat;
		background-size: cover;
		}
		.contactus #header {
		/* background: grey; */
		border-bottom: 1px solid darkgray;
		padding-top:20px;
		padding-bottom: 20px; 
		}
		.contactus #header p{
		color: #C5D5D4;
		font-style: italic;
		font-weight: bold;
		font-family: "Ropa Sans", sans-serif;
		font-size: 22px;
		}
		.contactus #content-right {
		margin-top: 20px;
		margin-right: 20px;
		width: 20%;
		float: right;
		}
		.contactus #content-left {
		margin-top: 20px;
		margin-right: 20px;
		width: 50%;
		float: left;
		border-right: grey 20px;
		}
		.contactus #content-left #contactbutton {
		width: 100px;
		height: 30px;
		background-color: grey;
		border: none;
		color:white;
		}
		.contactus #content-left #contactbutton:hover {
		background-color: darkgray;
		cursor: pointer;
		}
		.contactus #content-left p {
		font-family: "Ropa Sans", sans-serif;
		padding-right: 5px;
		padding-top: 5px;
		padding-bottom: 50px;
		font-size: 30px;
		text-align: center;
		}
		.contactus #content-right p {
		font-family: "Ropa Sans", sans-serif;
		padding-right: 5px;
		padding-top: 5px;
		padding-bottom: 5px;
		text-align: left;
		font-size: 20px;
		}
		.shipping {
		background: transparent;
		/* border: red 4px solid; */
		height: 600px;
		width: 100%;
		/* transform: translate(34%); */
		/* margin-top: 20px; */
		margin-bottom: 20px;
		/* padding-top: 20px; */
		height: 300px;
		}
		.shipping .banner #bannerimage {
		width: 100%;
		}
		.shipping #header {
		border-bottom: 1px solid darkgray;
		padding-top:20px;
		padding-bottom: 20px; 
		}
		.shipping #header p{
		color: rgb(7, 32, 31);
		font-style: italic;
		font-weight: bold;
		font-family: "Ropa Sans", sans-serif;
		font-size: 22px;
		}
		.shipping #content {
		/* padding-left: 30%; */
		padding-top: 80px;
		text-align: left;
		font-family: "Ropa Sans", sans-serif;
		}
		.shipping #content p {
			font-size: 30px;
			text-align: center;
			padding-top: 20px;
			color: white;
		}
		.shipping #content h3 {
			text-align: center;
			width:400px;
			margin: 0 auto;
			font-size: 50px;
			padding-bottom: 30px;
			color: white;
			border-bottom: red 1px solid;
		}
		.About {
		background: transparent;
		/* border: 4px solid red; */
		/* height: 600px; */
		width: 100%;
		/* padding-top: 70px; */
		/* margin-bottom: 20px; */
		/* height: 300px; */
		margin: 0 auto;
		}
		.About #bannerimage {
		width: 100%;
		}
		.About .text {
		text-align: left;
		/* padding-left: 30%; */
		padding-top: 70px;
		color: white;
		}
		.About .text p {
		font-size: 30px;
		text-align: center;
		padding-top: 20px;
		color: white;
		}
		.About .text #title {
		width: fit-content;
		margin: 0 auto;
		text-align: center;
		font-size: 50px;
		padding-bottom: 30px;
		border-bottom: red 1px solid;
		font-family: Exo, sans-serif;
		font-weight: bold;
		font-style: italic;
		text-transform: uppercase;
		text-shadow: 1px 1px #000;
		}
		.About #header {
		padding-top:20px;
		padding-bottom: 20px;
		color: #C5D5D4;
		font-style: italic;
		font-weight: bold;
		font-family: Exo, sans-serif;
		font-weight: bold;
		font-style: italic;
		text-transform: uppercase;
		text-shadow: 1px 1px #000;
		font-size: 20px;
		}
		/* .About #header p{
		color: #C5D5D4;
		font-style: italic;
		font-weight: bold;
		font-family: "Ropa Sans", sans-serif;
		font-size: 22px;
		} */
		.About #content p {
		padding-left: 5px;
		padding-top: 5px;
		padding-bottom: 5px;
		text-align: left;
		font-size: 20px;
		}
		.productexamples {
			display: flex;
			justify-content: space-evenly;
			width: 100%;
			/* height:700px; */
			transition: 0.5s ease-in-out;
			margin-bottom: 30px;
			/* padding-top: 100px; */
		}
		.productexamples #section1 {
			width: 650px;
			height: 650px;
			transition: 0.5s ease-in-out;
			/* background: black; */
			/* background: url(https://www.designbolts.com/wp-content/uploads/2012/11/Dark-Geometric-Semi-Dark-Seamleass-Pattern-for-website-backgrounds.jpg); */
		}
		.productexamples #section1 #description {
			opacity: 0;
			padding-bottom: 10px;
			width: 650px;
			height: 650px;
			transform: translate(0px, -650px);
			z-index: 2;
			position: relative;
			background: white;
			border: red 2px solid;
			padding-top: 3px;
			/* padding-left: 10px; */
			padding-right: 10px;
			transition: 0.2s ease-in-out;
			text-align: left;
			/* border-radius: 30px; */
		}
		.productexamples #section1 #description p {
			/* padding-top: 310px; */
			/* padding-left: 0px; */
			color: black;
			font-size: 15px;
		}
		.productexamples #section1:hover #description{
			transition: .75s ease-in-out;
			opacity: 1;
		}
		.productexamples #section1 #description:hover {
			visibility: visible;
		}
		.productexamples #section1 #description a {
			text-decoration: none;
		}
		.productexamples #section1 #description a h3:hover {
			transition: 0.5s ease-in-out;
			color:red;
		}
		.productexamples #section1 #description button {
			background-color: red;
			position: absolute;
			color: white;
			width: 150px;
			height: 50px;
			margin-top:90%;
			margin-left: 75%;
			font-size: 20px;
			border: transparent 1px solid;
		}
		.productexamples #section1 img {
			width:650;
			z-index: 2;
			position: relative;
			border: 2px solid white;
		}
		.productexamples #section1 #description button:hover{
			background-color: white;
			border: 1px red solid;
			color: red;
			transition: 0.5s ease-in-out;
		}
		.su-bg #RightPanel .lev1 li a p {
			width: 100%;
			text-align: left: ;;
			padding-bottom: 3px;
			border-bottom: transparent 1px solid;
		}
		.su-bg #RightPanel .lev1 li a p {
			width: 100%;
			text-align: left;
			padding-bottom: 3px;
			width: fit-content;
		}
		.su-bg #RightPanel .lev1 li a p:hover {
			/* text-decoration: underline;
			text-decoration-color: red; */
			transition: 0.5s ease-in-out;
			/* text-decoration: underline red; */
			border-bottom: red solid 1px;
		}
		.su-bg #su-head-whys img:hover {
			border-bottom: red 1px solid;
		}
		.menubar {
			width: 70%;
			/* max-width: 1000px; */
			/* margin-top: 15px; */
			margin-bottom: 5px;
			padding-top: 10px;
			float: top;
			max-width: 1330px;
			margin: 0 auto;
		}
		.menubar .contents {
			display: flex;
			justify-content: space-evenly;
		} 
		.menubar .contents .buttons {
			/* padding-bottom: 10px; */
			padding-top: 9px;
			text-align: center;
		}

		.menubar .contents .buttons .text {
			font-size: 30px;
			color: white;
			padding-bottom: 10px;
			transition: 0.5s ease-in-out;
		}

		.menubar .contents .buttons .text:hover{
			font-size: 30px;
			padding-bottom: 9px;
			border-bottom: red 1px solid;
			/* transition: 0.5s ease-in-out; */
			/* border-bottom: red 1px solid; */
		} 

		/* Cursed code that doesn't work so some reason -_- plz tell me why css gods */
		.menubar .contents .buttons .text:hover {
			/* padding-bottom: 9px; */
			background: white;
			border-bottom: red 1px solid;
		}
		
		.footer {
			width: 100%;
			height: 60px;
			background-color: white;
			display: flex;
			justify-content: space-evenly;
		}
		.footer .contents {
			padding-top:20px;
			transition: 0.5s ease-in-out;
		}
		.footer .contents a {
			border-bottom: transparent 1px solid
		}
		.footer .contents a {
			color: black;
			font-size: 20px;
			text-decoration: none;
		}
		.footer .contents a:hover {
			transition: 0.5s ease-in-out;
			border-bottom: red 1px solid;
		}

		#su-template.su-bg #su-main-gall h1:hover {
			transition: 0.5s ease-in-out;
			color: red;
		}

		.header {
			width: 100%;
			height: 100px;
			padding-top:30px;
		}

		.header .text {
			width: fit-content;
			margin: 0 auto;
		}

		.header .text p {
			color: white;
			font-size: 50px;
			border-bottom: red 1px solid;
			height: 43px;
			padding-left: 30px;
			padding-right: 30px;
			font-family: Exo, sans-serif;
			font-weight: bold;
			font-style: italic;
			text-transform: uppercase;
			text-shadow: 1px 1px #000;
		}


		@media screen and (max-width : 1024px) {    
    		.productexamples #section1 #description {
				visibility: visible;
			}
		}
		@media screen and (max-width: 1426px) {
			.shipping #content p {
				font-size: 20px;
				text-align: center;
				padding-top: 20px;
			}
			.shipping #content h3 {
				text-align: center;
				font-size: 40px;
				padding-bottom: 30px;
			}
			.About .text p {
				font-size: 20px;
				text-align: center;
				padding-top: 20px;
			}
			.About .text h3 {
				text-align: center;
				font-size: 40px;
				padding-bottom: 30px;
			}
			.productexamples {
				height:570px;
			}
			.productexamples #section1 img {
				width:570px;
			}
			.productexamples #section1 #description {
				width: 570px;
				height: 570px;
				transform: translate(0px, -570px);
			}
			.productexamples #section1 #description a h3{
				font-size: 15px;
			}
			.productexamples #section1 {
				width: 570px;
				height: 400px;
			}
			.productexamples #section1 #descriprion button{
				float: right;
				position: absolute;
			}
			.productexamples #section1 #description button {
				background-color: red;
				position: absolute;
				color: white;
				width: 150px;
				height: 50px;
				margin-top:88%;
				margin-left: 70%;
				font-size: 20px;
			}
		}



		@media screen and (max-width: 1200px){
			.productexamples #section1 #description button {
				opacity: 1;
			}
			.productexamples {
				height:520px;
			}
			.productexamples #section1 img {
				width:520px;
			}
			.productexamples #section1 #description {
				width: 520px;
				height: 520px;
				transform: translate(0px, -520px);
			}
			.productexamples #section1 #description a h3{
				font-size: 15px;
			}
			.productexamples #section1 {
				width: 520px;
				height: 520px;
			}
			.productexamples #section1 #descriprion button{
				float: right;
				position: absolute;
				margin-left: 57%;
			}
		}
		
		@media screen and (max-width: 1100px){
			.productexamples #section1 #description button {
				opacity: 1;
				margin-top: 85%;
				margin-left: 63%
			}
			.productexamples {
				height:450px;
			}
			.productexamples #section1 img {
				width:450px;
			}
			.productexamples #section1 #description {
				width: 450px;
				height: 450px;
				transform: translate(0px, -450px);
			}
			.productexamples #section1 #description a h3{
				font-size: 15px;
			}
			.productexamples #section1 {
				width: 450px;
				height: 450px;
			}
		}
		@media screen and (max-width: 900px){
			.productexamples #section1 #description button {
				opacity: 0;
			}
			.productexamples {
				height:420px;
			}
			.productexamples #section1 img {
				width:420px;
			}
			.productexamples #section1 #description {
				width: 420px;
				height: 420px;
				transform: translate(0px, -420px);
			}
			.productexamples #section1 #description a h3{
				font-size: 15px;
			}
			.productexamples #section1 {
				width: 420px;
				height: 420px;
			}
			.productexamples #section1 #descriprion button{
				float: right;
				position: absolute;
				margin-top: 40%;
				margin-left: 25%;
			}
		}
		@media screen and (max-width: 820px) {
			.shipping #content p {
				font-size: 20px;
				text-align: center;
				padding-top: 20px;
			}
			.shipping #content h3 {
				text-align: center;
				font-size: 40px;
				padding-bottom: 30px;
			}
			.About .text p {
				font-size: 20px;
				text-align: center;
				padding-top: 20px;
			}
			.About .text h3 {
				text-align: center;
				font-size: 40px;
				padding-bottom: 30px;
				border-bottom: red 1px solid;
			}
			.productexamples #section1 img {
				width:0px;
				padding-top: 150px;
			}
			.productexamples #section1 #description {
				width:370px;
				height: 490px;
				visibility: visible;
				border: black 3px solid;
				transform: translate(-10px, -160px);
				opacity: 1;
			}
			.productexamples #section1 #description p {
				padding-top: 160px;
			}
			.productexamples #section1 {
				width:350px;
				height: 280px;
			}
			.productexamples #section1 #description button {
				opacity: 0;
			}
		}
		@media screen and (max-width: 690px) {
		.shipping #content p {
			font-size: 20px;
			text-align: center;
			padding-top: 20px;
		}
		.shipping #content h3 {
			text-align: center;
			font-size: 40px;
			padding-bottom: 30px;
		}
		.About .text p {
			font-size: 20px;
			text-align: center;
			padding-top: 20px;
		}
		.About .text h3 {
			text-align: center;
			font-size: 40px;
			padding-bottom: 30px;
		}
		.productexamples #section1 img {
			width:0px;
			padding-top: 150px;
		}
		.productexamples #section1 #description {
			width:320px;
			height: 490px;
			opacity: 1;
			border: black 3px solid;
			transform: translate(-10px, -160px);
		}
		.productexamples #section1 #description p {
			padding-top: 160px;
		}
		.productexamples #section1 {
			width:350px;
			height: 280px;
		}
		.productexamples #section1 #description button {
				opacity: 0;
		}
}
		@media screen and (max-width: 1264){
		.contactus #content-right {
			width: 30%;
		}
		.About .text {
			padding-left: 20%;
		}
		}
		@media screen and (max-width: 1000px) {
		.product_carasel .controls #button1 {
			height: 150px;
		}
		.product_carasel .controls #button2 {
			height: 150px;
		}
		}
		@media screen and (max-width: 1344px) {
		.spacer {
			height: 1060px;
		}
		@media screen and (max-width: 1020px){
			.spacer {
				height: 50px;
			}
		}
		}
	</style>
<body>
			<div id="ds_div">
<meta name="viewport" cosuesu="width=device-width, initial-scale=1">
<link href="https://fonts.googleapis.com/css?family=Ropa+Sans:400,400i" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Exo:400,400i,700,700i" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.3.0/css/font-awesome.css">
<div id="su-template" class="su-bg"><div class="su-bg-02 su-shao">
		
<div id="su-head-wrap-02"><div id="su-head-02" class="su-content-width">
	<div id="su-head-logo" class="su-proh su-prom"><a href="https://www.ebay.com/str/simplyunlucky?rt=nc&_oac=1" target="_blank"><img src="https://raw.githubusercontent.com/Faveing/faveing.github.io/master/Banner%201.png" alt="simplyunlucky Games eBay Store"></a></div>
</div></div>
<div class="menubar">
	<div class="contents">
		<a class="buttons" id="link2" href="https://www.ebay.com/str/simplyunlucky?rt=nc&_oac=1" target="_blank"><p class="text">Store Home</p></a>
		<a class="buttons" id="link2" href="https://www.ebay.com/str/simplyunlucky/Store-Inventory/_i.html?_storecat=30717081014" target="_blank"><p class="text">Inventory</p></a>
		<a class="buttons" id="link3" href="https://www.ebay.com/str/simplyunlucky/YUGIOH-SINGLES/_i.html?_storecat=26691736014" target="_blank"><p class="text">Mixed Lots</p></a>
		<a class="buttons" id="link4" href="https://www.ebay.com/str/simplyunlucky/YUGIOH-SINGLES/_i.html?_storecat=26691736014" target="_blank"><p class="text">Singles</p></a>
	</div>
</div>
<div class="su-content">
<div id="RightPanel">
	<h4 id="su-side-tbar-cats" class="su-ttba su-fftb su-brdt su-bktt"><div class="su-tins su-ffac">YuGiOh Mixed Lots</div></h4>
	<div id="su-side-cats" class="su-sbox su-brdm su-bklt"><div class="su-tins">
		<ul class="lev1">
			<li><a target="_blank" href="https://www.ebay.com/itm/YUGIOH-50-CARD-ALL-HOLOGRAPHIC-HOLO-FOIL-COLLECTION-LOT-BONUS-10-FREE-FOILS/202810604138?hash=item2f38743a6a"><p id = "redhover" style="color:white;font-size: 17px;font-family: 'Times New Roman', Times, serif;">50 Foil Card Lot + Bonus 10 Foils</p></a></li>
		</ul>
	</div></div>
	<h4 id="su-side-tbar-cats" class="su-ttba su-fftb su-brdt su-bktt"><div class="su-tins su-ffac">YuGiOh Deck Lots</div></h4>
	<div id="su-side-cats" class="su-sbox su-brdm su-bklt"><div class="su-tins">
		<ul class="lev1">
			<li><a target="_blank" href="https://www.ebay.com/itm/DREAM-MIRROR-DECK-CHIM-RIRA-IKELOS-MORPHEUS-HYPNAGOGIA-ONEIROS-PHANTASOS-YuGiOh/202806528155?hash=item2f3836089b"><p style="color:white;font-size: 17px;font-family: 'Times New Roman', Times, serif;">Dream Mirror Deck CHIM RIRA: Ikelos Morpheus Hypnagogia Oneiros Phantasos YuGiOh</p></a></li>
		</ul>
	</div></div>
</div>
<div id="RightPanel" style="float: left; padding-right: 30px">
	<h4 id="su-side-tbar-cats" class="su-ttba su-fftb su-brdt su-bktt"><div class="su-tins su-ffac">YuGiOh Singles</div></h4>
	<div id="su-side-cats" class="su-sbox su-brdm su-bklt"><div class="su-tins">
			<ul class="lev1">
				<li><a target="_blank" href="https://www.ebay.com/str/simplyunlucky/SAST-Savage-Strike/_i.html?_storecat=27491324014&_sop=12"><p style="color:white;font-size: 16px; font-family: 'Times New Roman', Times, serif;">SAST Savage Strike</p></a></li>
						<li><a target="_blank" href="https://www.ebay.com/str/simplyunlucky/SOFU-Soul-Fusion/_i.html?_storecat=27311267014&_sop=12"><p style="color:white;font-size: 16px; font-family: 'Times New Roman', Times, serif;">SOFU Sour Fusion</p></a></li>
						<li><a target="_blank" href="https://www.ebay.com/str/simplyunlucky/CYHO-Cybernetic-Horizon/_i.html?_storecat=27311265014&_sop=12"><p style="color:white;font-size: 16px; font-family: 'Times New Roman', Times, serif;">CYHO Cybernetic Horizon</p></a></li>
						<li><a target="_blank" href="https://www.ebay.com/str/simplyunlucky/LED3-White-Dragon-Abyss/_i.html?_storecat=26691745014&_sop=12"><p style="color:white;font-size: 16px; font-family: 'Times New Roman', Times, serif;">LED3 White Dragon</p></a></li>
						<li><a target="_blank" href="https://www.ebay.com/str/simplyunlucky/LED4-Sisters-of-the-Rose/_i.html?_storecat=27359263014&_sop=12"><p style="color:white;font-size: 16px; font-family: 'Times New Roman', Times, serif;">LED4 Sisters of the Rose</p></a></li>
						<li><a target="_blank" href="https://www.ebay.com/str/simplyunlucky/SHVA-Shadows-in-Valhalla/_i.html?_storecat=26691746014&_sop=12"><p style="color:white;font-size: 16px; font-family: 'Times New Roman', Times, serif;">SHVA Shadows in Valhalla</p></a></li>
						<li><a target="_blank" href="https://www.ebay.com/str/simplyunlucky/HISU-Hidden-Summoners/_i.html?_storecat=26936014014&_sop=12"><p style="color:white;font-size: 16px; font-family: 'Times New Roman', Times, serif;">HISU Hidden Summoners</p></a></li>
						<li><a target="_blank" href="https://www.ebay.com/str/simplyunlucky/LEHD-Legendary-Hero-Decks/_i.html?_storecat=27684874014&_sop=12"><p style="color:white;font-size: 16px; font-family: 'Times New Roman', Times, serif;">LEHD Legendary Hero Decks</p></a></li>
						<li><a target="_blank" href="https://www.ebay.com/str/simplyunlucky/EXFO-Extreme-Force/_i.html?_storecat=27744394014&_sop=12"><p style="color:white;font-size: 16px; font-family: 'Times New Roman', Times, serif;">EXFO Extreme Force</p></a></li>
						<li><a target="_blank" href="https://www.ebay.com/str/simplyunlucky/SDSB-Structure-Deck-Soulburner/_i.html?_storecat=28072041014&_sop=12"><p style="color:white;font-size: 16px; font-family: 'Times New Roman', Times, serif;">SDSB Structure Deck:Soulburner</p></a></li>
						<li><a target="_blank" href="https://www.ebay.com/str/simplyunlucky/INCH-The-Infinity-Chasers/_i.html?_storecat=28078222014&_sop=12"><p style="color:white;font-size: 16px; font-family: 'Times New Roman', Times, serif;">INCH The Infinity Chasers</p></a></li>
						<li><a target="_blank" href="https://www.ebay.com/str/simplyunlucky/DUPO-Duel-Power/_i.html?_storecat=28280497014&_sop=12"><p style="color:white;font-size: 16px; font-family: 'Times New Roman', Times, serif;">DUPO Duel Power</p></a></li>
						<li><a target="_blank" href="https://www.ebay.com/str/simplyunlucky/SR08-Order-of-the-Spellcasters/_i.html?_storecat=28477561014&_sop=12"><p style="color:white;font-size: 16px; font-family: 'Times New Roman', Times, serif;">SRO8 Order of the Spellcasters</p></a></li>
						<li><a target="_blank" href="https://www.ebay.com/str/simplyunlucky/DANE-Dark-Neostorm/_i.html?_storecat=28603482014&_sop=12"><p style="color:white;font-size: 16px; font-family: 'Times New Roman', Times, serif;">DANE Dark Neostormv</p></a></li>
						<li><a target="_blank" href="https://www.ebay.com/str/simplyunlucky/BLHR-Heros-Revenge/_i.html?_storecat=29633992014&_sop=12"><p style="color:white;font-size: 16px; font-family: 'Times New Roman', Times, serif;">BLHR Hero's Revenge</p></a></li>
						<li><a target="_blank" href="https://www.ebay.com/str/simplyunlucky/FIGA-Fists-of-the-Gadgets/_i.html?_storecat=30164962014&_sop=12"><p style="color:white;font-size: 16px; font-family: 'Times New Roman', Times, serif;">FIGA Fists of the Gadgets</p></a></li>
						<li><a target="_blank" href="https://www.ebay.com/str/simplyunlucky/SDRR-Rokket-Revolt/_i.html?_storecat=30206730014&_sop=12"><p style="color:white;font-size: 16px; font-family: 'Times New Roman', Times, serif;">SDRR Rokket Revolt</p></a></li>
						<li><a target="_blank" href="https://www.ebay.com/str/simplyunlucky/MP19-Gold-Sarchophagus-Tin/_i.html?_storecat=30250539014&_sop=12"><p style="color:white;font-size: 16px; font-family: 'Times New Roman', Times, serif;">MP19 Gold Sarchophagus Tin</p></a></li>
						<li><a target="_blank" href="https://www.ebay.com/str/simplyunlucky/LED5-Immortal-Destiny/_i.html?_storecat=30499030014&_sop=12"><p style="color:white;font-size: 16px;font-family: 'Times New Roman', Times, serif;">LED5 Immortal Destiny</p></a></li>
						<li><a target="_blank" href="https://www.ebay.com/str/simplyunlucky/DUDE-Duel-Devastator/_i.html?_storecat=30568957014&_sop=12"><p style="color:white;font-size: 16px;font-family: 'Times New Roman', Times, serif;">DUDE Duel Devastator</p></a></li>
						<li><a target="_blank" href="https://www.ebay.com/str/simplyunlucky/CHIM-Chaos-Impact/_i.html?_storecat=30583833014&_sop=12"><p style="color:white;font-size: 16px;font-family: 'Times New Roman', Times, serif;">CHIM Chaos Impact</p></a></li>
			</ul>
		</div></div>
	<!-- <div id="su-side-sati" class="su-prom su-prot"><div class="su-tins">
		<img class="su-icon" src="su-icon-sati.png" alt="Satisfaction Guarasueed">
		<span>Satisfaction<span>100% Guarasueed</span></span>
	</div></div> -->
	
	<!-- <div id="su-side-ship" class="su-prom su-prot"><div class="su-tins">
		<img class="su-icon" src="nt-icon-ship.png" alt="Free Shipping">
		<span>Free Shipping<span>with order tracking</span></span>
	</div></div> -->
	
	<!-- left column spacer -->
</div>

<div id="su-main">
	<div id="su-main-gall" class="su-pbox su-brdm su-bklt"><div class="su-tins">
	
		<a href="" target="_blank" style="text-decoration: none; border: none;"><h1 id="MainHeader" style="border: none;">YUGIOH 50 CARD ALL HOLOGRAPHIC HOLO FOIL COLLECTION LOT! +BONUS 10 FREE FOILS!!&amp; RARES!</h1></a>
		
		<div id="su-temp-gall" class="su-bttm su-left">
			<div id="su-gall-main">
				<div id="mimg01"><input type="radio" id="img01" name="gallery" checked=""><div class="su-cntr"><img src="https://i.ebayimg.com/images/g/snsAAOSwt6RduJRf/s-l1600.jpg" alt=""></div></div>
				<div id="mimg02"><input type="radio" id="img02" name="gallery"><div class="su-cntr"><img src="https://i.ebayimg.com/images/g/39wAAOSw5LRduJRh/s-l1600.jpg" alt=""></div></div>
				<div id="mimg03"><input type="radio" id="img03" name="gallery"><div class="su-cntr"><img src="https://i.ebayimg.com/images/g/YWAAAOSwevJdudc8/s-l1600.jpg" alt=""></div></div>
				<div id="mimg04"><input type="radio" id="img04" name="gallery"><div class="su-cntr"><img src="https://i.ebayimg.com/images/g/YWAAAOSwevJdudc8/s-l1600.jpg" alt=""></div></div>
				<div id="mimg05"><input type="radio" id="img05" name="gallery"><div class="su-cntr"><img src="https://i.ebayimg.com/images/g/YWAAAOSwevJdudc8/s-l1600.jpg" alt=""></div></div>
				<div id="mimg06"><input type="radio" id="img06" name="gallery"><div class="su-cntr"><img src="" alt=""></div></div>
				<div id="mimg07"><input type="radio" id="img07" name="gallery"><div class="su-cntr"><img src="" alt=""></div></div>
				<div id="mimg08"><input type="radio" id="img08" name="gallery"><div class="su-cntr"><img src="" alt=""></div></div>
				<div id="mimg09"><input type="radio" id="img09" name="gallery"><div class="su-cntr"><img src="" alt=""></div></div>
				<div id="mimg10"><input type="radio" id="img10" name="gallery"><div class="su-cntr"><img src="" alt=""></div></div>
				<div id="mimg11"><input type="radio" id="img11" name="gallery"><div class="su-cntr"><img src="" alt=""></div></div>
				<div id="mimg12"><input type="radio" id="img12" name="gallery"><div class="su-cntr"><img src="" alt=""></div></div>
			</div>
		</div>
		<div id="su-gall-right">
<strong><big><font color="black"><u>Description</u></font></big></strong><br>
List of cards: Dream Mirror Hypnagogia x3<br>
Dream Mirror of Chaos x3<br>
Dream Mirror of Joy x3<br>
Dream Mirror of Terror x3<br>
Dream Mirror Oneiromancy x3<br>
Dream Mirror Phantasms x3<br>
Ikelos, The Dream Mirror Mara x3<br>
Morpheus, The Dream Mirror White Knight x3<br>
Oneiros, The Dream Mirror Erlking x3<br>
Phantasos, The Dream Mirror Foe x3<br>
Phantasos, The Dream Mirror Friend x3<br>
Dream Mirror Fantasy x3<br>
All of our singles are Mint/Near Mint! And SHIPPING is always FREE!!<br>
All cards are only guaranteed 1st edition when stated in the title<br>
Thank you for shopping!!!<br>
OH BABY!!<br>
-SU CORP<br>
</p>
	</div>
		<div id="su-gall-right" style="width: 100%;">
<strong><big><font color="black"><u>Customer Service</u></font></big></strong><br>
-Purchasing an order over $20 will guarantee priority processing with expedited handling and tracked shipping.<br>&nbsp;
-All cards are only guaranteed 1st Edition when stated in the title.<br>&nbsp;
-A listing with x3 in the title means you will receive 3 copies of the card named in that listing.<br>&nbsp;
-We always do our best to provide the best service possible. <br>&nbsp;
Before leaving a negative feedback please message us so we can help create a more positive experience for you.<br>&nbsp;
-Because of repeat offenders, please message us before making a purchase of over $20 if your account has below 5 feedback, thank you.<br>&nbsp;
-Check out our YouTube Channel for Unboxing Reviews of New and Classic YuGiOh Product!<br>&nbsp;
-Visit our Store for a more organized look at our MASSIVE INVENTORY of YuGiOh Cards!<br>&nbsp;
</p>
			</div></div>
		</div>
</div>

<div class="header">
	<div class="text">
		<p>CHECK OUT OUR OTHER PRODUCTS!</p>
	</div>
</div>

<!-- Product -->

<div class="productexamples">
	<div id="section1">
        <!-- Image link -->
        <!-- Link --> <a target="_blank" href='""" + product1_link + """'><!-- Link --> <!-- Image --><img id="img1" src="https://i.ebayimg.com/images/g/U9kAAOSwzxldsPPz/s-l1600.jpg"><!-- Image --></a>
        <!-- Image link -->

		<div id="description">
			<a href="""" + produck1_link + """" target="_blank"><button >View</button></a>
				<a href="""" + produck1_link + """" target="_blank"><h3 style="font-size: 20px;padding-top: 8px;padding-left: 40px;">DREAM MIRROR DECK CHIM RIRA: IKELOS MORPHEUS HYPNAGOGIA ONEIROS PHANTASOS YuGiOh</h3></a>
				<p style="padding-left: 40px;padding-top: 8px;"><!-- Description Text-->""" + product1_description + """
                        </p>
        </div>
	</div>
	<div id="section1">
		<!-- Image link -->
		<!-- Link --> <a target="_blank" href='"""+ product2_link + """'><!-- Link --> <!-- Image --><img src="https://i.ebayimg.com/images/g/Ld0AAOSw~8ldyY8V/s-l1600.jpg"><!-- Image --></a>
		<!-- Image link -->
		<div id="description">
			<a href="https://www.ebay.com/itm/GLADIATOR-BEAST-DECK-LOT-CHIM-Chaos-Impact-TEST-PANTHER-DOMITIANUS-YuGiOh/202805955335?hash=item2f382d4b07" target="_blank"><button >View</button></a>
				<a href="https://www.ebay.com/itm/GLADIATOR-BEAST-DECK-LOT-CHIM-Chaos-Impact-TEST-PANTHER-DOMITIANUS-YuGiOh/202805955335?hash=item2f382d4b07" target="_blank"><h3 style="font-size: 20px;padding-top: 8px;padding-left: 40px;">GLADIATOR BEAST DECK LOT | CHIM | Chaos Impact TEST PANTHER DOMITIANUS YuGiOh </h3></a>
				<p style="padding-left: 40px;padding-top: 8px;"><!-- Description Text-->""" + product2_link + """
					<!-- Description Text-->
						</p>
		</div>
	</div>
</div>

<!-- Product -->
<!-- Product -->

<div class="productexamples">
	<div id="section1">
		<!-- Image link -->
		<!-- Link --><a target="_blank" href='""" + product3_link + """'><!-- Link --> <!-- Image --><img id="img1" src="https://i.ebayimg.com/images/g/r1IAAOSwZEJdrm9A/s-l1600.jpg"><!-- Image --></a>
		<!-- Image link -->
		<div id="description">
			<a href='""" + product3_link + """' target="_blank"><button >View</button></a>
				<a href='""" + product3_link + """' target="_blank"><h3 style="font-size: 20px;padding-top: 8px;padding-left: 40px;">THUNDER DRAGON DECK LOT MP19 COLOSSUS TITAN DRAGONHAWK DRAGONDARK FUSION YuGiOh
				</h3></a>
				<p style="padding-left: 40px;padding-top: 8px;">
					<!-- Description Text-->"""+ product3_description + """
					<!-- Description Text-->
					</p>
		</div>
	</div>
	<div id="section1">
		<!-- Image link -->
		<!-- Link --><a target="_blank" href='"""+ product4_link + """'><!-- Link --> <!-- Image --><img id="img1" src="https://i.ebayimg.com/images/g/aM0AAOSwsvJdar3W/s-l1600.jpg"><!-- Image --></a>
		<!-- Image link -->
		<div id="description">
			<a href='""" + product4_link + """' target="_blank"><button >View</button></a>
				<a href='"""+ product4_link +"""' target="_blank"><h3 style="font-size: 20px;padding-top: 8px;padding-left: 40px;">VAMPIRE DECK LOT | MP19 SHERIDAN SUCKER FRAULEIN AWAKENING DOMINATION YuGiOh </h3></a>
				<p style="padding-left: 40px;padding-top: 8px;"> """ + product4_description + """
						</p>
		</div>
	</div>
</div>

<!-- Product -->

<div class="About" id="About">
	<div id="bannerimage">
	</div>
	<div class="text">
		<p id="title">About Us</p>
		<p>At SimplyUnlucky, YuGiOh fans are at the heart of everything we do.</p>
		<p>With them and our great partners, we help make the YuGiOh experience more extraordinary.</p>
	</div>
</div>
<div class="About" id="About">
	<div id="bannerimage">
	</div>
	<div class="text">
		<p id="title">Shipping Policy</p>
		<p>We will make sure every order get to its destination on time!</p>
	</div>
</div>

<div style="height:100px"></div>

</div>
<div class="footer">
	<div class="contents" id="col1">
		<a id="link" href="https://www.ebay.com/usr/simplyunlucky?_trksid=p2047675.l2559#" style="text-decoration: none;">Save our store!</a>
	</div>
	<div class="contents" id="col2">
		<a id="link" href="https://my.ebay.com/ws/eBayISAPI.dll?AcceptSavedSeller&_trksid=&linkname=includenewsletter&sellerid=simplyunlucky&guest=1">Subscribe</a>
	</div>
	<div class="contents" id="col3">
		<a id="link" href="https://contact.ebay.com/ws/eBayISAPI.dll?FindAnswers&requested=simplyunlucky&_trksid=p2545226.m2531.l4583&rt=nc">Suppport</a>
	</div>
</div>
</div></div></div>
</body>
</html>"""

    pyperclip.copy(newhtml)
    print(newhtml)

def Open():
    # filename = tk.filedialog.askopenfilename(title = "Select file", filetypes =(("Html Files", "*.html"),("All Files","*.*")))

    # print(filename)

    # textfile = open(filename, "r")

    # openedhtml = textfile.read()

    # print(get_product_link(openedhtml, 1, 1))

    # textdescription = product[1].split("<!-- Description Text-->")

    # update_products(get_product_link(openedhtml, 1, 1), get_product_description(openedhtml, 1, 1))

    # create_new_product_section()

    # draw_forms()

    # fill_forms(openedhtml)

    # print(openedhtml)

    edit_template("Test", "Test", product1_link.get(), product1_description.get(), product2_link.get(),product2_description.get(),product3_link.get(),product3_description.get(), product4_link.get(),product4_description.get())

def Logout():
    quit()

main_screen()

tk.mainloop()