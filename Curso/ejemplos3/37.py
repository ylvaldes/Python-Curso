#!/usr/bin/env python3
import sqlite3
class dbSebas:
    def __init__(self,dbname):
        if dbname:
            self._dbname=dbname
        self._dbfile=sqlite3.connect(self.dbname())
        self.dbfile().row_factory=sqlite3.Row
    def dbfile(self):
        return self._dbfile
    def dbname(self,n=None):
        if n:
            self._dbname=n
        try:
            return self._dbname
        except AttributeError:
            return 'unknown'
    def close(self):
        self.dbfile().close()
    def sql(self,q,p=()):
        s=self.dbfile()
        x=s.execute(q,p)
        s.commit()
        if x:
            return x
    def insert(self,t,x):
        k=sorted(x.keys())
        v=[x[i] for i in k]
        m='INSERT INTO {} ({}) VALUES ({})'
        q=m.format(t,','.join(k),','.join('?'*len(v)))
        self.sql(q,v)
    def drop(self,t):
        self.sql('DROP TABLE IF EXISTS {}'.format(t))
    def create(self,t,p):
        P='(id INTEGER PRIMARY KEY'
        for x in sorted(p):
            P=P+','+x+' '+p[x]
        P=P+')'
        m='CREATE TABLE {} {}'
        self.sql(m.format(t,P))
def main():
    n='37.db'
    t='numbers'
    t2='colors'
    p=dict(English='TEXT',Spanish='TEXT')
    x=[dict(English='one',Spanish='uno'),dict(English='two',Spanish='dos')]
    x2=[dict(English='red',Spanish='rojo')]
    d=dbSebas(n)
    d.drop(t)
    d.drop(t2)
    d.create(t,p)
    d.create(t2,p)
    for i in x:
        d.insert(t,i)
    for i in x2:
        d.insert(t2,i)
    for i in d.sql('SELECT * FROM {}'.format(t)):print('Table {}: {}'.format(t,dict(i)))
    for i in d.sql('SELECT * FROM {}'.format(t2)):print('Table {}: {}'.format(t2,tuple(i)))
    d.close()
if __name__=='__main__':main()
