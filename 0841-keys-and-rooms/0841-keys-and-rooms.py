class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vis = [False for i in range(len(rooms))]
        vis[0] = True 
        
        def dfs(room_num):
            temp = rooms[room_num]
            
            for i in temp:
                if vis[i] is False:
                    vis[i] = True
                    dfs(i)
                    
        dfs(0)
        
        if any(i == False for i in vis):
            return False
        else:
            return True