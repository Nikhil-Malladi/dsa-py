def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s_hmap,t_hmap = {}, {}

    for e1 in s:
        s_hmap[e1] = 1 +  s_hmap.get(e1,0)
    for e2 in t:
        t_hmap[e2] = 1 + t_hmap.get(e2,0)
    return s_hmap == t_hmap