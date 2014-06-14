import urllib.request
max_limit=10
def get_page(url):
    #print(url)
    try:
        f=urllib.request.Request(url)
        response=urllib.request.urlopen(f)
        page=response.read().decode('utf-8')
        return page
    except:
        return ""
    return ""

def union(a,b):
    for e in b:
        if e not in a :
            a.append(e)

def get_next_url(page):
	start_link=page.find("a href")
	if(start_link==-1):
		return None,0
	start_quote=page.find('"',start_link)
	end_quote=page.find('"',start_quote+1)
	url=page[start_quote+1:end_quote]
	return url,end_quote

    
def get_all_links(page):
	links=[]
	while(True):
		url,n=get_next_url(page)
		page=page[n:]
		if url:
			links.append(url)
		else:
			break
	return links

def look_up(index,keyword):
    if keyword in index:
        return index[keyword]
    return []


def add_to_index(index,url,keyword):

	if keyword in index:
		if url not in index[keyword]:
			index[keyword].append(url)
		return
	index[keyword]=[url]
	
def add_page_to_index(index,url,content):
    for i in content.split():
        add_to_index(index,url,i)

def compute_ranks(graph):
	d=0.8
	numloops=10
	ranks={}
	npages=len(graph)
	for page in graph:
		ranks[page]=1.0/npages
	for i in range(0,numloops):
		newranks={}
		for page in graph:
			newrank=(1-d)/npages
			for node in graph:
				if page in graph[node]:
					newrank=newrank+d*ranks[node]/len(graph[node])
			newranks[page]=newrank
		ranks=newranks
	return ranks

    
def crawl_web(seed):
    tocrawl=[seed]
    crawled=[]
    index={}
    graph={}
    global max_limit
    while(tocrawl):
        p=tocrawl.pop()
        if(p not in crawled):
            max_limit-=1
            #print(max_limit)
            if(max_limit<=0):
                break
            c=get_page(p)
            print(c)
            add_page_to_index(index,p,c)
            f=get_all_links(c)
            union(tocrawl,f)
            graph[p]=f
            crawled.append(p)
    return crawled,index,graph

def QuickSort(pages,ranks):
    if len(pages)>1 :
        pivot = ranks[pages[0]]
        i=1
        j=1
        for j in range(1,len(pages)):
            if(ranks[pages[j]]>pivot):
                pages[i],pages[j]=pages[j],pages[i]
                i+=1
        pages[i-1],pages[0]=pages[0],pages[i-1]
        QuickSort(pages[1:i],ranks)
        QuickSort(pages[i+1:len(pages)],ranks)

def look_up_new(index,ranks,keyword):
    pages=look_up(index,keyword)
    print('\nPrinting the results as is with page rank\n')
    for i in pages:
        print(i+" --> "+str(ranks[i]))
    QuickSort(pages,ranks)
    print('After Sorting the results by page rank\n')
    ret=0
    for i in pages:
        ret+=1
        print(str(ret)+'.\t'+i+'\n')


seed_page="http://en.wikipedia.org/wiki/Main_Page"
print("Enter the search item")
search_term=input()
#print('\nStarted crawling, presently at depth..')
crawled,index,graph=crawl_web(seed_page)
ranks=compute_ranks(graph)
look_up_new(index,ranks,search_term)
    
