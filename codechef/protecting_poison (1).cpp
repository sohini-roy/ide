#include <iostream>
#include <vector>

using namespace std;

struct snake{
    long hx,hy,tx,ty;
    bool used;
};

void rearrange(vector<snake> s,vector<snake> &h,vector<snake> &v,long start,long end){
  for(int i=0;i<s.size();i++){
    if(s[i].hx==s[i].tx){
      if((s[i].hy>=start && s[i].hy<=end) || (s[i].ty>=start && s[i].ty<=end) || (s[i].hy<=start && s[i].ty>=end))
        h.push_back(s[i]);
      else if(s[i].hx>=start && s[i].hx<=end)
        v.push_back(s[i]);
    }
    else{
      if((s[i].hx>=start && s[i].hx<=end) || (s[i].tx>=start && s[i].tx<=end) || (s[i].hx<=start && s[i].tx>=end))
        v.push_back(s[i]);
      else if(s[i].hy>=start && s[i].hy<=end)
        h.push_back(s[i]);
    }
  }
}

int find_minimum_snakes(vector<snake> &h,vector<snake> &v,long hor_start,long hor_end,long ver_start,long ver_end){
  int min_snakes = 0;
  while(hor_start<=hor_end){
    int longest=-1, length = 0;
    for(int i=0;i<h.size();i++){
      if(h[i].used == false && (hor_start>=h[i].hy && hor_start<=h[i].ty)){
        if(h[i].ty>=hor_end){
          longest = i;
          length = h[i].ty - hor_start + 1;
          break;
        }
        else if((h[i].ty - hor_start + 1) > length){
          longest = i;
          length = h[i].ty - hor_start + 1;
        }
      }
    }
    if(longest == -1)
      return -1;
    else{
      h[longest].used = true;
      min_snakes ++;
      hor_start+=length;
    }
  }

  while(ver_start<=ver_end){
    int longest=-1, length = 0;
    for(int i=0;i<v.size();i++){
      if(v[i].used == false && (ver_start>=v[i].hx && ver_start<=v[i].tx)){
        if(v[i].tx>=ver_end){
          longest = i;
          length = v[i].tx - ver_start + 1;
          break;
        }
        else if((v[i].tx - ver_start + 1) > length){
          longest = i;
          length = v[i].tx - ver_start + 1;
        }
      }
    }
    if(longest == -1)
      return -1;
    else{
      v[longest].used = true;
      min_snakes ++;
      ver_start+=length;
    }
  }
  return min_snakes;
}

int main() {
  int t;
  cin>>t;
  while(t){
    long n,k;
    int m;
    cin>>n>>k>>m;
    vector<snake> snakes(m);
    for(int i=0;i<m;i++){
      cin>>snakes[i].hx>>snakes[i].hy>>snakes[i].tx>>snakes[i].ty;
      snakes[i].used = false;
    }
    vector<snake> hor;
    vector<snake> vert;
    rearrange(snakes,hor,vert,((n-k)/2 + 1),((n+k)/2));
    int min_snakes = find_minimum_snakes(hor,vert,((n-k)/2 + 1),((n+k)/2),((n-k)/2 + 1),((n+k)/2));
    // cout<<"horizontal_exc:"<<endl;
    // for(int i=0;i<hor_exc.size();i++){
    //   cout<<hor_exc[i].hx<<" "<<hor_exc[i].hy<<" "<<hor_exc[i].tx<<" "<<hor_exc[i].ty<<" "<<hor_exc[i].used<<endl;
    // }
    cout<<min_snakes<<endl;
    t--;
  }
  return 0;
}
