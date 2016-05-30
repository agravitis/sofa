# scrape structube sofas

# load in teh whole infinite scroll then run
# jQuery.map(jQuery('.qview-btn-container'), function(x) { return {"prodId": jQuery(x.children[0]).attr('data-prod-id'), "parentId": jQuery(x.children[0]).attr('data-parent-id')}; });

# then run JSON.stringify on that result to get:

sofa_list = [{"prodId":"12760","parentId":"12759"},{"prodId":"12761","parentId":"12759"},{"prodId":"12762","parentId":"12759"},{"prodId":"12756","parentId":"12755"},{"prodId":"12757","parentId":"12755"},{"prodId":"12758","parentId":"12755"},{"prodId":"11094","parentId":"11093"},{"prodId":"11095","parentId":"11093"},{"prodId":"13009","parentId":"13688"},{"prodId":"17317","parentId":"17316"},{"prodId":"17321","parentId":"17320"},{"prodId":"17322","parentId":"17320"},{"prodId":"17323","parentId":"17320"},{"prodId":"17355","parentId":"17354"},{"prodId":"17356","parentId":"17354"},{"prodId":"17357","parentId":"17354"},{"prodId":"17873","parentId":"12676"},{"prodId":"17874","parentId":"12676"},{"prodId":"17875","parentId":"12679"},{"prodId":"17876","parentId":"12679"},{"prodId":"13010","parentId":"13688"},{"prodId":"13011","parentId":"13688"},{"prodId":"12681","parentId":"12679"},{"prodId":"12680","parentId":"12679"},{"prodId":"12678","parentId":"12676"},{"prodId":"12677","parentId":"12676"},{"prodId":"12802","parentId":"12801"},{"prodId":"11429","parentId":"11427"},{"prodId":"11430","parentId":"11427"},{"prodId":"11428","parentId":"11427"},{"prodId":"11431","parentId":"11427"},{"prodId":"12252","parentId":"12251"},{"prodId":"12253","parentId":"12251"},{"prodId":"12164","parentId":"12162"},{"prodId":"12165","parentId":"12162"},{"prodId":"12163","parentId":"12162"},{"prodId":"12166","parentId":"12162"},{"prodId":"12169","parentId":"12167"},{"prodId":"12170","parentId":"12167"},{"prodId":"12168","parentId":"12167"},{"prodId":"12171","parentId":"12167"},{"prodId":"11109","parentId":"11108"},{"prodId":"11110","parentId":"11108"},{"prodId":"12838","parentId":"12837"},{"prodId":"12840","parentId":"12839"},{"prodId":"12842","parentId":"12841"},{"prodId":"12844","parentId":"12843"},{"prodId":"12846","parentId":"12845"},{"prodId":"12848","parentId":"12847"},{"prodId":"12835","parentId":"12833"},{"prodId":"12877","parentId":"12876"},{"prodId":"13343","parentId":"13342"},{"prodId":"13345","parentId":"13344"},{"prodId":"13347","parentId":"13346"},{"prodId":"11386","parentId":"11383"},{"prodId":"11385","parentId":"11383"},{"prodId":"11384","parentId":"11383"},{"prodId":"11388","parentId":"11387"},{"prodId":"11389","parentId":"11387"},{"prodId":"11390","parentId":"11387"},{"prodId":"12618","parentId":"12617"},{"prodId":"12601","parentId":"12600"},{"prodId":"12599","parentId":"12598"},{"prodId":"12597","parentId":"12596"},{"prodId":"12595","parentId":"12594"},{"prodId":"12263","parentId":"12262"},{"prodId":"12259","parentId":"12258"},{"prodId":"12509","parentId":"12506"},{"prodId":"12508","parentId":"12506"},{"prodId":"12507","parentId":"12506"},{"prodId":"12896","parentId":"12894"},{"prodId":"12895","parentId":"12894"},{"prodId":"12257","parentId":"12254"},{"prodId":"12256","parentId":"12254"},{"prodId":"12255","parentId":"12254"},{"prodId":"12247","parentId":"12246"},{"prodId":"12608","parentId":"12606"},{"prodId":"12607","parentId":"12606"},{"prodId":"12928","parentId":"12771"},{"prodId":"12926","parentId":"12771"},{"prodId":"12061","parentId":"12058"},{"prodId":"12060","parentId":"12058"},{"prodId":"12059","parentId":"12058"},{"prodId":"12505","parentId":"12504"},{"prodId":"12610","parentId":"12609"},{"prodId":"12612","parentId":"12611"},{"prodId":"12499","parentId":"12498"},{"prodId":"12497","parentId":"12496"},{"prodId":"11325","parentId":"11322"},{"prodId":"11324","parentId":"11322"},{"prodId":"11323","parentId":"11322"},{"prodId":"13466","parentId":"13729"},{"prodId":"13467","parentId":"13729"},{"prodId":"13468","parentId":"13729"},{"prodId":"13205","parentId":"13603"},{"prodId":"13151","parentId":"13602"},{"prodId":"13101","parentId":"13601"},{"prodId":"13072","parentId":"13600"},{"prodId":"11368","parentId":"11366"},{"prodId":"11359","parentId":"11358"},{"prodId":"11361","parentId":"11358"},{"prodId":"11365","parentId":"11362"},{"prodId":"11363","parentId":"11362"},{"prodId":"11400","parentId":"11399"}]

import time
import urllib2

with open('sofas.json', 'a') as file:

    for sofa in sofa_list:
        product_id = sofa["prodId"]
        parent_id = sofa["parentId"]

        url = 'https://www.structube.com/en/absolunet_catalog/category_product/quickview/product_id/%s/parent_id/%s/' % (product_id, parent_id)
        print "Scraping: ", url
        response = urllib2.urlopen(url)
        html = response.read()
        file.write(html + '\n')

        time.sleep(0.3)
