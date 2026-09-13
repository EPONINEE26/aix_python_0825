class Students():

    slist=[]

    def add(self,s):
        self.slist.append(s)

    def set_rank(self):                             # ★ 등수 계산 (신규 추가 함수)
        ranked = sorted(self.slist, key=lambda s: s.total, reverse=True)
        rank = 0
        prev_total = None
        for i, s in enumerate(ranked, start=1):
            if s.total != prev_total:               # 총점이 다르면 등수 갱신
                rank = i
            s.rank = rank                            # 동점자는 같은 등수
            prev_total = s.total

    def print(self):
        self.set_rank()                              # ★ 출력 직전 등수 계산 호출
        print()
        print("-"*25, end="")
        print("[ 학생성적출력 ]")
        print("-"*60)
        print("번호","이름","국어","영어","수학","합계","평균","등수")   # ★ 등수 추가
        for s in self.slist:
            print(s)
