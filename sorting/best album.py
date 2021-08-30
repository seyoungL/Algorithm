# 베스트 앨범
# https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    from collections import defaultdict
    answer = []

    play_list = defaultdict(list)
    genres_cnt = defaultdict(int)
    
    # for i in range(len(genres)):
    #     play_list[genres[i]].append((plays[i],i))
    #     genres_cnt[genres[i]] += plays[i]

    for i, (g,p) in enumerate(zip(genres, plays)):
        play_list[g].append((p,i))
        genres_cnt[g] += p
        
    #for g, p in play_list.items():
    #    p.sort(key=lambda x:(-x[0], x[1]))    # [play cnt, idx], -x[0] = play cnt desc, x[1] = idx asc
    #    play_list[g] = p
        
    #genres_cnt = dict(sorted(genres_cnt.items(), key=lambda x :x[1], reverse=True))
    #for g,c in genres_cnt.items():
    for (g,c) in sorted(genres_cnt.items(), key=lambda x :x[1], reverse=True):
        play_list[g] = sorted(play_list[g], key=lambda x:(-x[0], x[1]))
        idx = [i for p,i in play_list[g]]
        
        #if(len(play_list[g]) < 2):
        #    answer.extend(idx)
        #else:
        answer.extend(idx[:2])
    
    return answer