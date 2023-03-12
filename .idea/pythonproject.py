import networkx as nx
import osmnx as ox
import folium
import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#start,stop변수 초기값 None으로 생성
start,stop = None, None

#버튼이 클릭되면, entry1의 문자열을 start변수에, entry2의 문자열을 stop변수에 저장 후 UI종료
def get_text():
    global start,stop
    start = text_entry1.get()
    stop = text_entry2.get()
    #인하대학교 정중앙 좌표값을 토대로 인하대학교 지도 생성
    latitude = 37.44940
    longitude = 126.65529
    m = folium.Map(location=[latitude, longitude], zoom_start=17)

    #wgs84좌표를 기준으로 각 node별 건물 이름과 좌표 coordinate 딕셔너리에 저장(지도 정보 볼 때 사용)
    coordinate = {}
    with open("inha_wgs84.txt", 'r', encoding='utf-8') as f:
        for _ in range(31):
            i,j,k = f.readline().split()
            if i == '정석학술정보관':
                folium.Marker([float(j),float(k)],
                              popup='<iframe width="800" height="500" src="https://lib.inha.ac.kr/kor">',
                              tooltip = i,
                              icon = folium.Icon(icon = 'info-sign')).add_to(m)
            elif '본관' in i:
                folium.Marker([float(j),float(k)],
                              popup= folium.Popup('<a href="https://www.inha.ac.kr/kr/1073/subview.do">교직원식당 식단표</a><br>총장실 860-7000',
                                                  parse_html=False,
                                                  max_width=1000),
                              tooltip = i,
                              icon = folium.Icon(icon = 'info-sign')).add_to(m)
            elif '6호관' in i:
                folium.Marker([float(j), float(k)],
                              popup=folium.Popup('아태물류학부 860-8222<br>여학생 휴게실3(6호관 118)',
                                                  parse_html=False,
                                                  max_width=1000),
                tooltip = i,
                icon = folium.Icon(icon = 'info-sign')).add_to(m)

            elif '7호관' in i:
                folium.Marker([float(j), float(k)],
                              popup=folium.Popup('학사관리팀 860-7041~8<br>예비군연대본부 860-8309',
                                                  parse_html=False,
                                                  max_width=1000),
                tooltip = i,
                icon = folium.Icon(icon = 'info-sign')).add_to(m)

            elif '학생식당,하나은행' in i:
                folium.Marker([float(j), float(k)],
                              popup=folium.Popup('<a href="https://www.inha.ac.kr/kr/1072/subview.do">학생식당 식단표</a><br>서점 860-9143<br>안경점 070-8844-1001<br>써브웨이 070-8835-3277<br>더카페 861-7172<br>세븐일레븐 861-7172<br>IROMGYM 010-7499-7504',
                                                  parse_html=False,
                                                  max_width=1000),
                tooltip = i,
                icon = folium.Icon(icon = 'info-sign')).add_to(m)
                
            elif '9호관' in i:
                folium.Marker([float(j), float(k)],
                              popup=folium.Popup('사회과학대학 860-7902',
                                                  parse_html=False,
                                                  max_width=1000),
                tooltip = i,
                icon = folium.Icon(icon = 'info-sign')).add_to(m)
            elif '60주년기념관' in i:
                folium.Marker([float(j),float(k)],
                              popup= folium.Popup('의예과 860-8190<br>화학공학과 860-7460',
                                                  parse_html=False,
                                                  max_width=1000),
                              tooltip = i,
                              icon = folium.Icon(icon = 'info-sign')).add_to(m)
            elif '2북관' in i:
                folium.Marker([float(j),float(k)],
                              popup= folium.Popup('환경공학과 860-7500<br>공과대학행정실 860-7284~90<br>여학생 휴게실1 (2남 240)<br>기계공학과 860-7300<br>산업경영공학과 860-7360<br>고분자공학과 860-7480<br>남학생 휴게실 (2북 273)',
                                                  parse_html=False,
                                                  max_width=1000),
                              tooltip = i,
                              icon = folium.Icon(icon = 'info-sign')).add_to(m)
            elif '4호관' in i:
                folium.Marker([float(j),float(k)],
                              popup= folium.Popup('공간정보공학과 860-7600',
                                                  parse_html=False,
                                                  max_width=1000),
                              tooltip = i,
                              icon = folium.Icon(icon = 'info-sign')).add_to(m)
            elif '5호관' in i:
                folium.Marker([float(j),float(k)],
                              popup= folium.Popup('간호학과 860-8200<br>스포츠과학과 860-8180<br>한국어문학과 860-7990<br>중국학과 860-8050<br>여학생 휴게실2 (5남 130)<br>신소재공학부 860-7520<br>통계학 860-7640',
                                                  parse_html=False,
                                                  max_width=1000),
                              tooltip = i,
                              icon = folium.Icon(icon = 'info-sign')).add_to(m)
            elif '하이테크센터' in i:
                folium.Marker([float(j),float(k)],
                              popup= folium.Popup('전기공학과 860-7390<br>전자공학과 860-7410<br>컴퓨터공학과 860-7457<br>여학생 휴게실4(하이테크 100)',
                                                  parse_html=False,
                                                  max_width=1000),
                              tooltip = i,
                              icon = folium.Icon(icon = 'info-sign')).add_to(m)
            elif '제1생활관' in i:
                folium.Marker([float(j),float(k)],
                              popup= folium.Popup('제1생활관행정실 860-8317',
                                                  parse_html=False,
                                                  max_width=1000),
                              tooltip = i,
                              icon = folium.Icon(icon = 'info-sign')).add_to(m)
            elif '제2,3생활관' in i:
                folium.Marker([float(j),float(k)],
                              popup= folium.Popup('생활관행정팀 860-8317,7273',
                                                  parse_html=False,
                                                  max_width=1000),
                              tooltip = i,
                              icon = folium.Icon(icon = 'info-sign')).add_to(m)
            elif '김현태' in i:
                folium.Marker([float(j),float(k)],
                              popup= folium.Popup('창업보육센터 860-7252',
                                                  parse_html=False,
                                                  max_width=1000),
                              tooltip = i,
                              icon = folium.Icon(icon = 'info-sign')).add_to(m)
            elif '서호관,나빌레관' in i:
                folium.Marker([float(j),float(k)],
                              popup= folium.Popup('사범대 860-7833',
                                                  parse_html=False,
                                                  max_width=1000),
                              tooltip = i,
                              icon = folium.Icon(icon = 'info-sign')).add_to(m)
            elif '학군단' in i:
                folium.Marker([float(j),float(k)],
                              popup= folium.Popup('행정실 860-8332',
                                                  parse_html=False,
                                                  max_width=1000),
                              tooltip = i,
                              icon = folium.Icon(icon = 'info-sign')).add_to(m)
            elif '로스쿨관' in i:
                folium.Marker([float(j),float(k)],
                              popup= folium.Popup('법학연구소 860-8649',
                                                  parse_html=False,
                                                  max_width=1000),
                              tooltip = i,
                              icon = folium.Icon(icon = 'info-sign')).add_to(m)
            else:
                folium.Marker([float(j),float(k)], tooltip = i).add_to(m)

    #html로 지도 저장
    m.save('map.html')

    #UTM좌표를 기준으로 각 node별 건물 이름과 좌표 coordinate_UTM 딕셔너리에 저장(길찾기 할 때 사용)
    coordinate_UTM = {}
    with open("inha_UTM.txt", 'r', encoding='utf-8') as f:
        for _ in range(31):
            i,j,k = f.readline().split()
            coordinate_UTM[i] = [j,k]

    #길찾기 경로 표시를 위해 osmnx로 지도 좌표에 따른 node와 edge 생성
    G = ox.graph_from_point((latitude,longitude), dist_type='network', network_type='walk')
    # fig, ax = ox.plot_graph(G)

    #UTM좌표로 변환된 지도 좌표
    G_proj = ox.project_graph(G)

    #입력받은 출발점,도착점 좌표 지정
    orig_node = ox.nearest_nodes(G_proj, float(coordinate_UTM[start][0]), float(coordinate_UTM[start][1]))
    dest_node = ox.nearest_nodes(G_proj, float(coordinate_UTM[stop][0]), float(coordinate_UTM[stop][1]))

    #최단거리 검색 후 거리 길이 및 소요시간(기준 : 4km/h) 저장
    route = nx.shortest_path(G, orig_node, dest_node, weight='length')
    len = nx.shortest_path_length(G, orig_node, dest_node, weight='length')
    len = round(len,1)
    time = round(len/66.7,1)


    #지도 11시 방향에 소요거리 및 소요시간 표시
    m.get_root().html.add_child(folium.Element("""
    <div style="position : fixed;
    left:50px;top:0px;
    width : 300px;
    line-height : 0px;
    background-color : white;
    z-index : 1000">
    <h1 style="font-size : 30px;">소요 거리 : {0}미터</h1><br/>
    <h1 style="font-size : 30px;">소요 시간 : {1}분</h1>
    </div>
    """.format(len,time)))

    #최단거리를 지도정보를 저장한 파일(route_map = m)에 덮어쓴 후 저장
    route_graph_map = ox.plot_route_folium(G, route, route_map=m, popup_attribute='length')
    route_graph_map.save('route.html')
    webbrowser.open_new('route.html')    

#UI 생성
root = tk.Tk()
root.geometry("600x200")
root.title("네비게이션")
root.resizable(False, False) #사이즈 조절 X

frame = tk.Frame(root)
frame.pack()

scroll_bar=Scrollbar(root)

#맨 왼쪽 박스(출발지 입력)
text_label1=tk.Label(frame,
    text="출발지 입력",
    width=8,
    font=('맑은 고딕',16,'bold'),
    bg='#2F5597',
    fg='white')
text_label1.grid(row=0, column=0,padx=5,pady=10)

#1행에 있는 화살표
text_label2=tk.Label(frame,text='\u2192',
                          font=('맑은 고딕',11,'bold'),
                          bg="white",
                          fg='black',
                          width=8)
text_label2.grid(row=0, column=1,padx=5,pady=10)

#2행 박스("도착지 입력")
text_label3=tk.Label(frame,
    text="도착지 입력",
    width=8,
    font=('맑은 고딕',16,'bold'),
    bg='#2F5597',
    fg='white')
text_label3.grid(row=1, column=0,padx=5,pady=10)

#2행의 화살표
text_label4=tk.Label(frame,text='\u2192',
                          font=('맑은 고딕',11,'bold'),
                          bg="white",
                          fg='black',
                          width=8)
text_label4.grid(row=1, column=1,padx=5,pady=10)

#1행 콤보박스
text_entry1=ttk.Combobox(frame, width=30, textvariable=start)
text_entry1['values']=('후문', '하이테크쪽문', '하이테크센터', '학생식당,하나은행', '7호관',
                       '인경호', '2북관-북쪽', '2북관-남쪽', '4호관', '2남관', '60주년기념관'
                       '5호관-동쪽-1', '5호관-동쪽-2', '5호관-남쪽', '서호관,나빌레관', '비룡주차장',
                       '정석학술정보관', '로스쿨관', '테니스장', '대운동장,농구장', '학군단', '정문',
                       '평생교육원,미융대', '9호관', '6호관', '김현태인하드림센터', '본관-북쪽',
                       '본관-남쪽', '카페Grazie', '제1생활관', '제2,3생활관(비룡재)')
text_entry1.grid(row=0, column=2, padx=5,pady=10)
text_entry1.current(0)

#2행 콤보박스
text_entry2=ttk.Combobox(frame, width=30, textvariable=stop)
text_entry2['values']=('후문', '하이테크쪽문', '하이테크센터', '학생식당,하나은행', '7호관',
                       '인경호', '2북관-북쪽', '2북관-남쪽', '4호관', '2남관', '60주년기념관'
                       '5호관-동쪽-1', '5호관-동쪽-2', '5호관-남쪽', '서호관,나빌레관', '비룡주차장',
                       '정석학술정보관', '로스쿨관', '테니스장', '대운동장,농구장', '학군단', '정문',
                       '평생교육원,미융대', '9호관', '6호관', '김현태인하드림센터', '본관-북쪽',
                       '본관-남쪽', '카페Grazie', '제1생활관', '제2,3생활관(비룡재)')
text_entry2.grid(row=1, column=2, padx=5,pady=10)
text_entry2.current(0)

#버튼
button = tk.Button(frame, text = '경로 입력', font=('맑은 고딕',16,'bold'),
                   command = get_text)
button.grid(row=2, column=2, sticky="sw")


root.mainloop()
