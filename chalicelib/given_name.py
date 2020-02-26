import random

def get_random() -> (str, str):
    ary = all()
    a = ary[random.randrange(len(ary))]
    return a[0], a[1]

def all():
    return [
        ['のり子', 'のりこ'],
        ['ひろ子', 'ひろこ'],
        ['まり子', 'まりこ'],
        ['れい子', 'れいこ'],
        ['亜衣', 'あい'],
        ['亜希', 'あき'],
        ['亜希子', 'あきこ'],
        ['亜紀', 'あき'],
        ['亜実', 'あみ'],
        ['亜樹', 'あき'],
        ['亜美', 'あみ'],
        ['亜矢', 'あや'],
        ['亜矢子', 'あやこ'],
        ['愛', 'あい'],
        ['愛', 'めぐみ'],
        ['愛子', 'あいこ'],
        ['愛実', 'まなみ'],
        ['愛美', 'まなみ'],
        ['愛梨', 'あいり'],
        ['愛理', 'あいり'],
        ['愛里', 'あいり'],
        ['葵', 'あおい'],
        ['茜', 'あかね'],
        ['旭', 'あきら'],
        ['梓', 'あずさ'],
        ['綾', 'あや'],
        ['綾香', 'あやか'],
        ['綾子', 'あやこ'],
        ['綾乃', 'あやの'],
        ['杏子', 'きょうこ'],
        ['杏奈', 'あんな'],
        ['杏里', 'あんり'],
        ['依子', 'よりこ'],
        ['郁', 'かおる'],
        ['郁子', 'いくこ'],
        ['郁美', 'いくみ'],
        ['郁夫', 'いくお'],
        ['一', 'はじめ'],
        ['一義', 'かずよし'],
        ['一浩', 'かずひろ'],
        ['一樹', 'かずき'],
        ['一将', 'かずまさ'],
        ['一真', 'かずま'],
        ['一成', 'いっせい'],
        ['一成', 'かずなり'],
        ['一生', 'いっせい'],
        ['一馬', 'かずま'],
        ['一美', 'かずみ'],
        ['一彦', 'かずひこ'],
        ['一夫', 'かずお'],
        ['一也', 'かずや'],
        ['一雄', 'かずお'],
        ['一海', 'かずみ'],
        ['一洋', 'かずひろ'],
        ['一朗', 'いちろう'],
        ['一郎', 'いちろう'],
        ['映子', 'えいこ'],
        ['栄一', 'えいいち'],
        ['栄作', 'えいさく'],
        ['栄子', 'えいこ'],
        ['栄治', 'えいじ'],
        ['栄二', 'えいじ'],
        ['英一', 'えいいち'],
        ['英恵', 'はなえ'],
        ['英司', 'えいじ'],
        ['英子', 'えいこ'],
        ['英治', 'えいじ'],
        ['英樹', 'ひでき'],
        ['英世', 'ひでよ'],
        ['英二', 'えいじ'],
        ['英之', 'ひでゆき'],
        ['英彦', 'ひでひこ'],
        ['英夫', 'ひでお'],
        ['英明', 'ひであき'],
        ['英雄', 'ひでお'],
        ['悦子', 'えつこ'],
        ['温子', 'あつこ'],
        ['佳子', 'けいこ'],
        ['佳子', 'よしこ'],
        ['佳代', 'かよ'],
        ['佳代子', 'かよこ'],
        ['佳奈', 'かな'],
        ['佳祐', 'けいすけ'],
        ['加奈', 'かな'],
        ['加奈子', 'かなこ'],
        ['夏海', 'なつみ'],
        ['夏希', 'なつき'],
        ['夏子', 'なつこ'],
        ['夏実', 'なつみ'],
        ['夏樹', 'なつき'],
        ['夏美', 'なつみ'],
        ['花音', 'かのん'],
        ['華子', 'はなこ'],
        ['雅', 'みやび'],
        ['雅弘', 'まさひろ'],
        ['雅子', 'まさこ'],
        ['雅樹', 'まさき'],
        ['雅俊', 'まさとし'],
        ['雅人', 'まさと'],
        ['雅之', 'まさゆき'],
        ['雅美', 'まさみ'],
        ['雅彦', 'まさひこ'],
        ['雅也', 'まさや'],
        ['絵美', 'えみ'],
        ['絵理', 'えり'],
        ['絵里', 'えり'],
        ['馨', 'かおる'],
        ['学', 'がく'],
        ['学', 'まなぶ'],
        ['寛', 'ひろし'],
        ['寛子', 'ひろこ'],
        ['寛之', 'ひろゆき'],
        ['巌', 'いわお'],
        ['希', 'のぞみ'],
        ['毅', 'たけし'],
        ['毅', 'つよし'],
        ['紀子', 'のりこ'],
        ['貴', 'たかし'],
        ['貴久', 'たかひさ'],
        ['貴宏', 'たかひろ'],
        ['貴幸', 'たかゆき'],
        ['貴広', 'たかひろ'],
        ['貴司', 'たかし'],
        ['貴史', 'たかし'],
        ['貴史', 'たかふみ'],
        ['貴子', 'たかこ'],
        ['貴志', 'たかし'],
        ['貴大', 'たかひろ'],
        ['貴之', 'たかゆき'],
        ['貴博', 'たかひろ'],
        ['貴美子', 'きみこ'],
        ['貴彦', 'たかひこ'],
        ['貴也', 'たかや'],
        ['貴裕', 'たかひろ'],
        ['貴洋', 'たかひろ'],
        ['輝', 'あきら'],
        ['輝彦', 'てるひこ'],
        ['輝明', 'てるあき'],
        ['輝雄', 'てるお'],
        ['義久', 'よしひさ'],
        ['義孝', 'よしたか'],
        ['義弘', 'よしひろ'],
        ['義浩', 'よしひろ'],
        ['義行', 'よしゆき'],
        ['義人', 'よしと'],
        ['義則', 'よしのり'],
        ['義男', 'よしお'],
        ['義之', 'よしゆき'],
        ['義彦', 'よしひこ'],
        ['義明', 'よしあき'],
        ['義雄', 'よしお'],
        ['義隆', 'よしたか'],
        ['久', 'ひさし'],
        ['久子', 'ひさこ'],
        ['久美', 'くみ'],
        ['久美子', 'くみこ'],
        ['久雄', 'ひさお'],
        ['弓子', 'ゆみこ'],
        ['亨', 'とおる'],
        ['京子', 'きょうこ'],
        ['強', 'つよし'],
        ['恭一', 'きょういち'],
        ['恭子', 'きょうこ'],
        ['恭兵', 'きょうへい'],
        ['恭平', 'きょうへい'],
        ['響子', 'きょうこ'],
        ['暁', 'さとる'],
        ['勤', 'つとむ'],
        ['均', 'ひとし'],
        ['勲', 'いさお'],
        ['薫', 'かおる'],
        ['啓介', 'けいすけ'],
        ['啓子', 'けいこ'],
        ['啓太', 'けいた'],
        ['啓二', 'けいじ'],
        ['啓之', 'ひろゆき'],
        ['圭', 'けい'],
        ['圭一', 'けいいち'],
        ['圭介', 'けいすけ'],
        ['圭吾', 'けいご'],
        ['圭子', 'けいこ'],
        ['圭二', 'けいじ'],
        ['圭佑', 'けいすけ'],
        ['圭祐', 'けいすけ'],
        ['恵', 'めぐみ'],
        ['恵一', 'けいいち'],
        ['恵介', 'けいすけ'],
        ['恵子', 'けいこ'],
        ['恵二', 'けいじ'],
        ['恵美', 'えみ'],
        ['恵美', 'めぐみ'],
        ['恵美子', 'えみこ'],
        ['恵理', 'えり'],
        ['恵理子', 'えりこ'],
        ['恵里', 'えり'],
        ['慶', 'けい'],
        ['慶子', 'けいこ'],
        ['慶太', 'けいた'],
        ['慶彦', 'よしひこ'],
        ['敬', 'たかし'],
        ['敬一', 'けいいち'],
        ['敬介', 'けいすけ'],
        ['敬子', 'けいこ'],
        ['敬太郎', 'けいたろう'],
        ['景子', 'けいこ'],
        ['桂子', 'けいこ'],
        ['潔', 'きよし'],
        ['結衣', 'ゆい'],
        ['健', 'けん'],
        ['健', 'たけし'],
        ['健一', 'けんいち'],
        ['健一郎', 'けんいちろう'],
        ['健介', 'けんすけ'],
        ['健吾', 'けんご'],
        ['健司', 'けんじ'],
        ['健児', 'けんじ'],
        ['健次', 'けんじ'],
        ['健次郎', 'けんじろう'],
        ['健人', 'けんと'],
        ['健太', 'けんた'],
        ['健太朗', 'けんたろう'],
        ['健太郎', 'けんたろう'],
        ['健二', 'けんじ'],
        ['憲', 'けん'],
        ['憲一', 'けんいち'],
        ['憲司', 'けんじ'],
        ['憲治', 'けんじ'],
        ['研二', 'けんじ'],
        ['謙一', 'けんいち'],
        ['謙介', 'けんすけ'],
        ['謙治', 'けんじ'],
        ['謙太', 'けんた'],
        ['謙太郎', 'けんたろう'],
        ['賢', 'けん'],
        ['賢', 'まさる'],
        ['賢一', 'けんいち'],
        ['賢治', 'けんじ'],
        ['賢人', 'けんと'],
        ['賢太郎', 'けんたろう'],
        ['賢二', 'けんじ'],
        ['元', 'げん'],
        ['元気', 'げんき'],
        ['五郎', 'ごろう'],
        ['悟', 'さとる'],
        ['護', 'まもる'],
        ['光', 'ひかる'],
        ['光一', 'こういち'],
        ['光弘', 'みつひろ'],
        ['光浩', 'みつひろ'],
        ['光司', 'こうじ'],
        ['光子', 'みつこ'],
        ['光太郎', 'こうたろう'],
        ['光代', 'みつよ'],
        ['光夫', 'みつお'],
        ['光雄', 'みつお'],
        ['公子', 'きみこ'],
        ['公彦', 'きみひこ'],
        ['公平', 'こうへい'],
        ['功', 'いさお'],
        ['厚', 'あつし'],
        ['孝', 'たかし'],
        ['孝一', 'こういち'],
        ['孝幸', 'たかゆき'],
        ['孝弘', 'たかひろ'],
        ['孝行', 'たかゆき'],
        ['孝子', 'たかこ'],
        ['孝志', 'たかし'],
        ['孝二', 'こうじ'],
        ['孝之', 'たかゆき'],
        ['孝明', 'たかあき'],
        ['孝雄', 'たかお'],
        ['宏', 'ひろし'],
        ['宏一', 'こういち'],
        ['宏治', 'こうじ'],
        ['宏樹', 'ひろき'],
        ['宏美', 'ひろみ'],
        ['巧', 'たくみ'],
        ['幸一', 'こういち'],
        ['幸一郎', 'こういちろう'],
        ['幸弘', 'ゆきひろ'],
        ['幸司', 'こうじ'],
        ['幸子', 'さちこ'],
        ['幸子', 'ゆきこ'],
        ['幸男', 'ゆきお'],
        ['幸二', 'こうじ'],
        ['幸夫', 'ゆきお'],
        ['幸平', 'こうへい'],
        ['幸雄', 'ゆきお'],
        ['広幸', 'ひろゆき'],
        ['広樹', 'ひろき'],
        ['広大', 'こうだい'],
        ['広明', 'ひろあき'],
        ['広和', 'ひろかず'],
        ['康', 'やすし'],
        ['康一', 'こういち'],
        ['康介', 'こうすけ'],
        ['康幸', 'やすゆき'],
        ['康弘', 'やすひろ'],
        ['康子', 'やすこ'],
        ['康成', 'やすなり'],
        ['康晴', 'やすはる'],
        ['康太', 'こうた'],
        ['康二', 'こうじ'],
        ['康博', 'やすひろ'],
        ['康夫', 'やすお'],
        ['康平', 'こうへい'],
        ['康雄', 'やすお'],
        ['弘', 'ひろし'],
        ['弘幸', 'ひろゆき'],
        ['弘子', 'ひろこ'],
        ['弘樹', 'ひろき'],
        ['弘美', 'ひろみ'],
        ['弘明', 'ひろあき'],
        ['晃', 'あきら'],
        ['晃一', 'こういち'],
        ['晃司', 'こうじ'],
        ['晃子', 'あきこ'],
        ['晃平', 'こうへい'],
        ['浩', 'ひろし'],
        ['浩一', 'こういち'],
        ['浩一郎', 'こういちろう'],
        ['浩介', 'こうすけ'],
        ['浩幸', 'ひろゆき'],
        ['浩三', 'こうぞう'],
        ['浩司', 'こうじ'],
        ['浩史', 'ひろし'],
        ['浩子', 'ひろこ'],
        ['浩治', 'こうじ'],
        ['浩二', 'こうじ'],
        ['浩之', 'ひろゆき'],
        ['浩美', 'ひろみ'],
        ['浩平', 'こうへい'],
        ['耕一', 'こういち'],
        ['耕二', 'こうじ'],
        ['耕平', 'こうへい'],
        ['航平', 'こうへい'],
        ['香菜', 'かな'],
        ['香織', 'かおり'],
        ['高史', 'たかし'],
        ['高志', 'たかし'],
        ['剛', 'ごう'],
        ['剛', 'たけし'],
        ['剛', 'つよし'],
        ['剛史', 'つよし'],
        ['豪', 'ごう'],
        ['克己', 'かつみ'],
        ['克行', 'かつゆき'],
        ['克彦', 'かつひこ'],
        ['克也', 'かつや'],
        ['今日子', 'きょうこ'],
        ['佐知子', 'さちこ'],
        ['佐和子', 'さわこ'],
        ['沙織', 'さおり'],
        ['沙耶香', 'さやか'],
        ['彩', 'あや'],
        ['彩夏', 'あやか'],
        ['彩花', 'あやか'],
        ['彩香', 'あやか'],
        ['彩子', 'あやこ'],
        ['彩子', 'さいこ'],
        ['彩乃', 'あやの'],
        ['菜摘', 'なつみ'],
        ['菜穂子', 'なほこ'],
        ['桜子', 'さくらこ'],
        ['三四郎', 'さんしろう'],
        ['三枝子', 'みえこ'],
        ['三郎', 'さぶろう'],
        ['司', 'つかさ'],
        ['史子', 'ふみこ'],
        ['史郎', 'しろう'],
        ['四郎', 'しろう'],
        ['志保', 'しほ'],
        ['志穂', 'しほ'],
        ['詩織', 'しおり'],
        ['次郎', 'じろう'],
        ['治', 'おさむ'],
        ['治子', 'はるこ'],
        ['七海', 'ななみ'],
        ['七瀬', 'ななせ'],
        ['実', 'みのる'],
        ['若菜', 'わかな'],
        ['守', 'まもる'],
        ['朱美', 'あけみ'],
        ['寿', 'ひさし'],
        ['樹里', 'じゅり'],
        ['周作', 'しゅうさく'],
        ['周平', 'しゅうへい'],
        ['修', 'おさむ'],
        ['修一', 'しゅういち'],
        ['修司', 'しゅうじ'],
        ['修二', 'しゅうじ'],
        ['修平', 'しゅうへい'],
        ['秀一', 'しゅういち'],
        ['秀幸', 'ひでゆき'],
        ['秀子', 'ひでこ'],
        ['秀樹', 'ひでき'],
        ['秀昭', 'ひであき'],
        ['秀人', 'ひでと'],
        ['秀典', 'ひでのり'],
        ['秀徳', 'ひでのり'],
        ['秀夫', 'ひでお'],
        ['秀平', 'しゅうへい'],
        ['秀明', 'ひであき'],
        ['秀雄', 'ひでお'],
        ['秀和', 'ひでかず'],
        ['充', 'みつる'],
        ['俊', 'しゅん'],
        ['俊一', 'しゅんいち'],
        ['俊英', 'としひで'],
        ['俊介', 'しゅんすけ'],
        ['俊哉', 'としや'],
        ['俊作', 'しゅんさく'],
        ['俊樹', 'としき'],
        ['俊太郎', 'しゅんたろう'],
        ['俊二', 'しゅんじ'],
        ['俊之', 'としゆき'],
        ['俊彦', 'としひこ'],
        ['俊夫', 'としお'],
        ['俊輔', 'しゅんすけ'],
        ['俊明', 'としあき'],
        ['俊雄', 'としお'],
        ['春菜', 'はるな'],
        ['春樹', 'はるき'],
        ['春奈', 'はるな'],
        ['春雄', 'はるお'],
        ['駿', 'しゅん'],
        ['淳', 'あつし'],
        ['淳', 'じゅん'],
        ['淳一', 'じゅんいち'],
        ['淳子', 'じゅんこ'],
        ['淳平', 'じゅんぺい'],
        ['淳也', 'じゅんや'],
        ['潤', 'じゅん'],
        ['潤一郎', 'じゅんいちろう'],
        ['純', 'じゅん'],
        ['純一', 'じゅんいち'],
        ['純子', 'じゅんこ'],
        ['純平', 'じゅんぺい'],
        ['順', 'じゅん'],
        ['順子', 'じゅんこ'],
        ['渚', 'なぎさ'],
        ['勝', 'まさる'],
        ['勝己', 'かつみ'],
        ['勝弘', 'かつひろ'],
        ['勝成', 'かつなり'],
        ['勝則', 'かつのり'],
        ['勝太', 'しょうた'],
        ['勝男', 'かつお'],
        ['勝彦', 'かつひこ'],
        ['勝巳', 'かつみ'],
        ['勝也', 'かつや'],
        ['匠', 'たくみ'],
        ['将志', 'まさし'],
        ['将人', 'まさと'],
        ['将太', 'しょうた'],
        ['将大', 'まさひろ'],
        ['将之', 'まさゆき'],
        ['将彦', 'まさひこ'],
        ['小春', 'こはる'],
        ['小百合', 'さゆり'],
        ['尚', 'ひさし'],
        ['尚子', 'なおこ'],
        ['彰', 'あきら'],
        ['昇', 'のぼる'],
        ['昇平', 'しょうへい'],
        ['昌宏', 'まさひろ'],
        ['昌幸', 'まさゆき'],
        ['昌弘', 'まさひろ'],
        ['昌子', 'まさこ'],
        ['昌彦', 'まさひこ'],
        ['昌平', 'しょうへい'],
        ['昌也', 'まさや'],
        ['昭', 'あきら'],
        ['昭一', 'しょういち'],
        ['昭子', 'あきこ'],
        ['昭二', 'しょうじ'],
        ['昭彦', 'あきひこ'],
        ['昭夫', 'あきお'],
        ['晶子', 'あきこ'],
        ['梢', 'こずえ'],
        ['渉', 'わたる'],
        ['祥', 'しょう'],
        ['祥吾', 'しょうご'],
        ['祥子', 'しょうこ'],
        ['祥子', 'さちこ'],
        ['祥平', 'しょうへい'],
        ['章', 'あきら'],
        ['章子', 'あきこ'],
        ['譲', 'ゆずる'],
        ['伸', 'しん'],
        ['伸一', 'しんいち'],
        ['伸介', 'しんすけ'],
        ['伸幸', 'のぶゆき'],
        ['伸治', 'しんじ'],
        ['伸二', 'しんじ'],
        ['伸也', 'しんや'],
        ['信', 'しん'],
        ['信一', 'しんいち'],
        ['信介', 'しんすけ'],
        ['信吾', 'しんご'],
        ['信子', 'のぶこ'],
        ['信二', 'しんじ'],
        ['信之', 'のぶゆき'],
        ['信彦', 'のぶひこ'],
        ['信夫', 'のぶお'],
        ['信也', 'しんや'],
        ['信雄', 'のぶお'],
        ['慎一', 'しんいち'],
        ['慎一郎', 'しんいちろう'],
        ['慎吾', 'しんご'],
        ['慎司', 'しんじ'],
        ['慎太郎', 'しんたろう'],
        ['慎二', 'しんじ'],
        ['慎也', 'しんや'],
        ['新', 'あらた'],
        ['新一', 'しんいち'],
        ['新太郎', 'しんたろう'],
        ['晋', 'すすむ'],
        ['晋也', 'しんや'],
        ['晋太郎', 'しんたろう'],
        ['真', 'まこと'],
        ['真衣', 'まい'],
        ['真一', 'しんいち'],
        ['真一郎', 'しんいちろう'],
        ['真央', 'まお'],
        ['真希', 'まき'],
        ['真紀', 'まき'],
        ['真紀子', 'まきこ'],
        ['真弓', 'まゆみ'],
        ['真琴', 'まこと'],
        ['真吾', 'しんご'],
        ['真司', 'しんじ'],
        ['真治', 'しんじ'],
        ['真実', 'まみ'],
        ['真樹', 'まき'],
        ['真人', 'まさと'],
        ['真澄', 'ますみ'],
        ['真太郎', 'しんたろう'],
        ['真知子', 'まちこ'],
        ['真奈美', 'まなみ'],
        ['真二', 'しんじ'],
        ['真之介', 'しんのすけ'],
        ['真帆', 'まほ'],
        ['真美', 'まみ'],
        ['真也', 'しんや'],
        ['真由', 'まゆ'],
        ['真由子', 'まゆこ'],
        ['真由美', 'まゆみ'],
        ['真理', 'まり'],
        ['真理子', 'まりこ'],
        ['進', 'すすむ'],
        ['進一', 'しんいち'],
        ['仁', 'じん'],
        ['仁', 'ひとし'],
        ['仁志', 'ひとし'],
        ['仁美', 'ひとみ'],
        ['瑞希', 'みずき'],
        ['瑞穂', 'みずほ'],
        ['崇', 'たかし'],
        ['崇史', 'たかし'],
        ['成美', 'なるみ'],
        ['政信', 'まさのぶ'],
        ['政夫', 'まさお'],
        ['晴香', 'はるか'],
        ['晴子', 'はるこ'],
        ['晴美', 'はるみ'],
        ['晴彦', 'はるひこ'],
        ['正', 'ただし'],
        ['正一', 'しょういち'],
        ['正紀', 'まさのり'],
        ['正義', 'まさよし'],
        ['正孝', 'まさたか'],
        ['正宏', 'まさひろ'],
        ['正幸', 'まさゆき'],
        ['正浩', 'まさひろ'],
        ['正行', 'まさゆき'],
        ['正三', 'しょうぞう'],
        ['正志', 'まさし'],
        ['正治', 'まさはる'],
        ['正樹', 'まさき'],
        ['正昭', 'まさあき'],
        ['正人', 'まさと'],
        ['正人', 'まさひと'],
        ['正則', 'まさのり'],
        ['正男', 'まさお'],
        ['正典', 'まさのり'],
        ['正博', 'まさひろ'],
        ['正美', 'まさみ'],
        ['正彦', 'まさひこ'],
        ['正敏', 'まさとし'],
        ['正夫', 'まさお'],
        ['正巳', 'まさみ'],
        ['正明', 'まさあき'],
        ['正洋', 'まさひろ'],
        ['正隆', 'まさたか'],
        ['正和', 'まさかず'],
        ['清', 'きよし'],
        ['清美', 'きよみ'],
        ['清隆', 'きよたか'],
        ['聖子', 'しょうこ'],
        ['聖子', 'せいこ'],
        ['誠', 'まこと'],
        ['誠一', 'せいいち'],
        ['誠一郎', 'せいいちろう'],
        ['誠司', 'せいじ'],
        ['誠治', 'せいじ'],
        ['誠二', 'せいじ'],
        ['静', 'しずか'],
        ['静香', 'しずか'],
        ['節', 'たかし'],
        ['節子', 'せつこ'],
        ['千佳', 'ちか'],
        ['千夏', 'ちなつ'],
        ['千絵', 'ちえ'],
        ['千恵', 'ちえ'],
        ['千恵子', 'ちえこ'],
        ['千秋', 'ちあき'],
        ['千春', 'ちはる'],
        ['千晶', 'ちあき'],
        ['千尋', 'ちひろ'],
        ['千晴', 'ちはる'],
        ['千穂', 'ちほ'],
        ['千明', 'ちあき'],
        ['千里', 'ちさと'],
        ['泉', 'いずみ'],
        ['創', 'はじめ'],
        ['早紀', 'さき'],
        ['早苗', 'さなえ'],
        ['聡', 'さとし'],
        ['聡', 'さとる'],
        ['聡', 'そう'],
        ['聡子', 'さとこ'],
        ['聡美', 'さとみ'],
        ['太', 'ふとし'],
        ['太一', 'たいち'],
        ['太一郎', 'たいちろう'],
        ['太朗', 'たろう'],
        ['太郎', 'たろう'],
        ['泰弘', 'やすひろ'],
        ['泰三', 'たいぞう'],
        ['泰子', 'やすこ'],
        ['大', 'だい'],
        ['大介', 'だいすけ'],
        ['大貴', 'だいき'],
        ['大輝', 'だいき'],
        ['大五郎', 'だいごろう'],
        ['大作', 'だいさく'],
        ['大志', 'たいし'],
        ['大樹', 'たいき'],
        ['大樹', 'だいき'],
        ['大樹', 'ひろき'],
        ['大助', 'だいすけ'],
        ['大地', 'だいち'],
        ['大輔', 'だいすけ'],
        ['大和', 'やまと'],
        ['卓', 'すぐる'],
        ['卓也', 'たくや'],
        ['卓郎', 'たくろう'],
        ['拓', 'たく'],
        ['拓哉', 'たくや'],
        ['拓馬', 'たくま'],
        ['拓也', 'たくや'],
        ['拓弥', 'たくや'],
        ['拓矢', 'たくや'],
        ['拓郎', 'たくろう'],
        ['琢磨', 'たくま'],
        ['琢也', 'たくや'],
        ['達哉', 'たつや'],
        ['達夫', 'たつお'],
        ['達也', 'たつや'],
        ['達朗', 'たつろう'],
        ['達郎', 'たつろう'],
        ['辰徳', 'たつのり'],
        ['辰夫', 'たつお'],
        ['辰也', 'たつや'],
        ['知宏', 'ともひろ'],
        ['知哉', 'ともや'],
        ['知子', 'ともこ'],
        ['知美', 'ともみ'],
        ['智', 'さとし'],
        ['智', 'とも'],
        ['智久', 'ともひさ'],
        ['智恵', 'ちえ'],
        ['智恵子', 'ちえこ'],
        ['智弘', 'ともひろ'],
        ['智子', 'ともこ'],
        ['智子', 'さとこ'],
        ['智之', 'ともゆき'],
        ['智博', 'ともひろ'],
        ['智美', 'ともみ'],
        ['智彦', 'ともひこ'],
        ['智也', 'ともや'],
        ['智洋', 'ともひろ'],
        ['忠', 'ただし'],
        ['忠志', 'ただし'],
        ['忠夫', 'ただお'],
        ['忠雄', 'ただお'],
        ['直輝', 'なおき'],
        ['直哉', 'なおや'],
        ['直子', 'なおこ'],
        ['直樹', 'なおき'],
        ['直人', 'なおと'],
        ['直美', 'なおみ'],
        ['直也', 'なおや'],
        ['通', 'とおる'],
        ['哲', 'さとし'],
        ['哲', 'さとる'],
        ['哲', 'てつ'],
        ['哲哉', 'てつや'],
        ['哲司', 'てつじ'],
        ['哲男', 'てつお'],
        ['哲夫', 'てつお'],
        ['哲也', 'てつや'],
        ['哲朗', 'てつろう'],
        ['哲郎', 'てつろう'],
        ['徹', 'とおる'],
        ['徹也', 'てつや'],
        ['鉄平', 'てっぺい'],
        ['鉄也', 'てつや'],
        ['典子', 'のりこ'],
        ['登', 'のぼる'],
        ['都', 'みやこ'],
        ['努', 'つとむ'],
        ['桃', 'もも'],
        ['桃子', 'ももこ'],
        ['透', 'とおる'],
        ['瞳', 'ひとみ'],
        ['道子', 'みちこ'],
        ['道夫', 'みちお'],
        ['道雄', 'みちお'],
        ['篤', 'あつし'],
        ['篤司', 'あつし'],
        ['篤史', 'あつし'],
        ['篤志', 'あつし'],
        ['敦', 'あつし'],
        ['敦史', 'あつし'],
        ['敦士', 'あつし'],
        ['敦子', 'あつこ'],
        ['奈々', 'なな'],
        ['奈々子', 'ななこ'],
        ['奈央', 'なお'],
        ['奈月', 'なつき'],
        ['奈緒', 'なお'],
        ['奈緒美', 'なおみ'],
        ['奈津子', 'なつこ'],
        ['奈津美', 'なつみ'],
        ['奈美', 'なみ'],
        ['南', 'みなみ'],
        ['二朗', 'じろう'],
        ['二郎', 'じろう'],
        ['忍', 'しのぶ'],
        ['博', 'ひろし'],
        ['博一', 'ひろかず'],
        ['博行', 'ひろゆき'],
        ['博司', 'ひろし'],
        ['博史', 'ひろし'],
        ['博子', 'ひろこ'],
        ['博志', 'ひろし'],
        ['博樹', 'ひろき'],
        ['博之', 'ひろゆき'],
        ['博美', 'ひろみ'],
        ['博文', 'ひろふみ'],
        ['肇', 'はじめ'],
        ['八郎', 'はちろう'],
        ['隼', 'じゅん'],
        ['隼人', 'はやと'],
        ['繁', 'しげる'],
        ['美佳', 'みか'],
        ['美加', 'みか'],
        ['美希', 'みき'],
        ['美紀', 'みき'],
        ['美貴', 'みき'],
        ['美恵子', 'みえこ'],
        ['美幸', 'みゆき'],
        ['美香', 'みか'],
        ['美佐', 'みさ'],
        ['美佐子', 'みさこ'],
        ['美沙子', 'みさこ'],
        ['美咲', 'みさき'],
        ['美子', 'よしこ'],
        ['美樹', 'みき'],
        ['美緒', 'みお'],
        ['美織', 'みおり'],
        ['美代子', 'みよこ'],
        ['美智子', 'みちこ'],
        ['美津子', 'みつこ'],
        ['美奈', 'みな'],
        ['美奈子', 'みなこ'],
        ['美帆', 'みほ'],
        ['美保', 'みほ'],
        ['美穂', 'みほ'],
        ['美穂子', 'みほこ'],
        ['美也子', 'みやこ'],
        ['美優', 'みゆう'],
        ['美由紀', 'みゆき'],
        ['美里', 'みさと'],
        ['美和', 'みわ'],
        ['美和子', 'みわこ'],
        ['百合子', 'ゆりこ'],
        ['敏', 'さとし'],
        ['敏行', 'としゆき'],
        ['敏子', 'としこ'],
        ['敏之', 'としゆき'],
        ['敏夫', 'としお'],
        ['敏郎', 'としろう'],
        ['富士夫', 'ふじお'],
        ['武', 'たけし'],
        ['武司', 'たけし'],
        ['武史', 'たけし'],
        ['武志', 'たけし'],
        ['武夫', 'たけお'],
        ['舞', 'まい'],
        ['舞子', 'まいこ'],
        ['文', 'あや'],
        ['文子', 'あやこ'],
        ['文子', 'ふみこ'],
        ['文彦', 'ふみひこ'],
        ['文夫', 'ふみお'],
        ['文雄', 'ふみお'],
        ['勉', 'つとむ'],
        ['勉', 'べん'],
        ['保', 'たもつ'],
        ['歩', 'あゆみ'],
        ['歩', 'あゆむ'],
        ['歩美', 'あゆみ'],
        ['朋子', 'ともこ'],
        ['朋美', 'ともみ'],
        ['法子', 'のりこ'],
        ['芳雄', 'よしお'],
        ['萌', 'もえ'],
        ['豊', 'ゆたか'],
        ['豊和', 'とよかず'],
        ['邦子', 'くにこ'],
        ['邦彦', 'くにひこ'],
        ['邦夫', 'くにお'],
        ['望', 'のぞみ'],
        ['望', 'のぞむ'],
        ['北斗', 'ほくと'],
        ['麻衣', 'まい'],
        ['麻衣子', 'まいこ'],
        ['麻希', 'まき'],
        ['麻子', 'あさこ'],
        ['麻帆', 'まほ'],
        ['麻美', 'あさみ'],
        ['麻美', 'まみ'],
        ['麻由', 'まゆ'],
        ['麻由子', 'まゆこ'],
        ['麻里', 'まり'],
        ['万里', 'まり'],
        ['満', 'みつる'],
        ['未来', 'みく'],
        ['未来', 'みらい'],
        ['稔', 'みのる'],
        ['妙子', 'たえこ'],
        ['明', 'あきら'],
        ['明久', 'あきひさ'],
        ['明宏', 'あきひろ'],
        ['明子', 'あきこ'],
        ['明日香', 'あすか'],
        ['明美', 'あけみ'],
        ['明彦', 'あきひこ'],
        ['明夫', 'あきお'],
        ['茂', 'しげる'],
        ['茂樹', 'しげき'],
        ['茂雄', 'しげお'],
        ['猛', 'たけし'],
        ['弥生', 'やよい'],
        ['靖', 'やすし'],
        ['靖子', 'やすこ'],
        ['唯', 'ゆい'],
        ['佑介', 'ゆうすけ'],
        ['佑樹', 'ゆうき'],
        ['優', 'すぐる'],
        ['優', 'まさる'],
        ['優', 'ゆう'],
        ['優一', 'ゆういち'],
        ['優花', 'ゆうか'],
        ['優介', 'ゆうすけ'],
        ['優希', 'ゆうき'],
        ['優香', 'ゆうか'],
        ['優作', 'ゆうさく'],
        ['優子', 'ゆうこ'],
        ['優太', 'ゆうた'],
        ['優也', 'ゆうや'],
        ['勇', 'いさむ'],
        ['勇一', 'ゆういち'],
        ['勇介', 'ゆうすけ'],
        ['勇気', 'ゆうき'],
        ['勇輝', 'ゆうき'],
        ['勇樹', 'ゆうき'],
        ['勇人', 'はやと'],
        ['勇人', 'ゆうと'],
        ['勇太', 'ゆうた'],
        ['勇二', 'ゆうじ'],
        ['友', 'ゆう'],
        ['友紀', 'ゆき'],
        ['友香', 'ゆか'],
        ['友子', 'ともこ'],
        ['友信', 'とものぶ'],
        ['友美', 'ともみ'],
        ['友美', 'ゆみ'],
        ['友里', 'ゆり'],
        ['友和', 'ともかず'],
        ['悠', 'はるか'],
        ['悠', 'ゆう'],
        ['悠太', 'ゆうた'],
        ['悠平', 'ゆうへい'],
        ['有希', 'ゆうき'],
        ['有希', 'ゆき'],
        ['有希子', 'ゆきこ'],
        ['有紀', 'ゆき'],
        ['有紀子', 'ゆきこ'],
        ['有香', 'ゆか'],
        ['有沙', 'ありさ'],
        ['有紗', 'ありさ'],
        ['有美', 'ゆみ'],
        ['由衣', 'ゆい'],
        ['由佳', 'ゆか'],
        ['由紀', 'ゆき'],
        ['由紀子', 'ゆきこ'],
        ['由貴', 'ゆき'],
        ['由起子', 'ゆきこ'],
        ['由香', 'ゆか'],
        ['由香里', 'ゆかり'],
        ['由実', 'ゆみ'],
        ['由美', 'ゆみ'],
        ['由美子', 'ゆみこ'],
        ['由梨', 'ゆり'],
        ['由里子', 'ゆりこ'],
        ['祐一', 'ゆういち'],
        ['祐介', 'ゆうすけ'],
        ['祐希', 'ゆうき'],
        ['祐輝', 'ゆうき'],
        ['祐司', 'ゆうじ'],
        ['祐子', 'ゆうこ'],
        ['祐樹', 'ゆうき'],
        ['祐太', 'ゆうた'],
        ['祐二', 'ゆうじ'],
        ['祐美子', 'ゆみこ'],
        ['祐輔', 'ゆうすけ'],
        ['裕', 'ひろし'],
        ['裕', 'ゆたか'],
        ['裕一', 'ゆういち'],
        ['裕一郎', 'ゆういちろう'],
        ['裕介', 'ゆうすけ'],
        ['裕幸', 'ひろゆき'],
        ['裕行', 'ひろゆき'],
        ['裕哉', 'ゆうや'],
        ['裕司', 'ゆうじ'],
        ['裕子', 'ひろこ'],
        ['裕子', 'ゆうこ'],
        ['裕次', 'ゆうじ'],
        ['裕樹', 'ゆうき'],
        ['裕太', 'ゆうた'],
        ['裕二', 'ゆうじ'],
        ['裕之', 'ひろゆき'],
        ['裕美', 'ひろみ'],
        ['裕美子', 'ゆみこ'],
        ['裕也', 'ゆうや'],
        ['雄一', 'ゆういち'],
        ['雄一郎', 'ゆういちろう'],
        ['雄介', 'ゆうすけ'],
        ['雄貴', 'ゆうき'],
        ['雄三', 'ゆうぞう'],
        ['雄太', 'ゆうた'],
        ['雄大', 'ゆうた'],
        ['雄大', 'ゆうだい'],
        ['雄二', 'ゆうじ'],
        ['雄也', 'ゆうや'],
        ['雄祐', 'ゆうすけ'],
        ['夕貴', 'ゆき'],
        ['夕子', 'ゆうこ'],
        ['容子', 'ようこ'],
        ['庸介', 'ようすけ'],
        ['曜子', 'ようこ'],
        ['洋', 'ひろし'],
        ['洋一', 'よういち'],
        ['洋一郎', 'よういちろう'],
        ['洋介', 'ようすけ'],
        ['洋子', 'ようこ'],
        ['洋次郎', 'ようじろう'],
        ['洋之', 'ひろゆき'],
        ['洋平', 'ようへい'],
        ['洋輔', 'ようすけ'],
        ['洋祐', 'ようすけ'],
        ['葉子', 'ようこ'],
        ['要', 'かなめ'],
        ['遥', 'はるか'],
        ['陽一', 'よういち'],
        ['陽一郎', 'よういちろう'],
        ['陽介', 'ようすけ'],
        ['陽子', 'ようこ'],
        ['陽平', 'ようへい'],
        ['翼', 'つばさ'],
        ['藍', 'あい'],
        ['藍子', 'あいこ'],
        ['蘭', 'らん'],
        ['利明', 'としあき'],
        ['梨絵', 'りえ'],
        ['梨紗', 'りさ'],
        ['梨奈', 'りな'],
        ['理', 'おさむ'],
        ['理恵', 'りえ'],
        ['理沙', 'りさ'],
        ['理子', 'りこ'],
        ['理紗', 'りさ'],
        ['里佳', 'りか'],
        ['里香', 'りか'],
        ['里沙', 'りさ'],
        ['里奈', 'りな'],
        ['陸', 'りく'],
        ['律子', 'りつこ'],
        ['留美', 'るみ'],
        ['隆', 'たかし'],
        ['隆一', 'りゅういち'],
        ['隆弘', 'たかひろ'],
        ['隆行', 'たかゆき'],
        ['隆史', 'たかし'],
        ['隆志', 'たかし'],
        ['隆治', 'りゅうじ'],
        ['隆太', 'りゅうた'],
        ['隆太郎', 'りゅうたろう'],
        ['隆二', 'りゅうじ'],
        ['隆之', 'たかゆき'],
        ['竜一', 'りゅういち'],
        ['竜司', 'りゅうじ'],
        ['竜次', 'りゅうじ'],
        ['竜太', 'りゅうた'],
        ['竜二', 'りゅうじ'],
        ['竜也', 'たつや'],
        ['龍', 'りゅう'],
        ['龍一', 'りゅういち'],
        ['龍太郎', 'りゅうたろう'],
        ['龍二', 'りゅうじ'],
        ['龍之介', 'りゅうのすけ'],
        ['亮', 'りょう'],
        ['亮介', 'りょうすけ'],
        ['亮太', 'りょうた'],
        ['亮平', 'りょうへい'],
        ['亮輔', 'りょうすけ'],
        ['涼', 'りょう'],
        ['涼介', 'りょうすけ'],
        ['涼子', 'りょうこ'],
        ['涼太', 'りょうた'],
        ['涼平', 'りょうへい'],
        ['良', 'りょう'],
        ['良一', 'りょういち'],
        ['良子', 'りょうこ'],
        ['良太', 'りょうた'],
        ['良太郎', 'りょうたろう'],
        ['良平', 'りょうへい'],
        ['諒', 'りょう'],
        ['遼', 'りょう'],
        ['力', 'ちから'],
        ['力也', 'りきや'],
        ['緑', 'みどり'],
        ['瑠衣', 'るい'],
        ['瑠美', 'るみ'],
        ['塁', 'るい'],
        ['令子', 'れいこ'],
        ['玲', 'れい'],
        ['玲子', 'れいこ'],
        ['玲奈', 'れいな'],
        ['玲奈', 'れな'],
        ['礼子', 'れいこ'],
        ['麗子', 'れいこ'],
        ['麗奈', 'れな'],
        ['廉', 'れん'],
        ['朗', 'あきら'],
        ['和歌子', 'わかこ'],
        ['和義', 'かずよし'],
        ['和久', 'かずひさ'],
        ['和恵', 'かずえ'],
        ['和宏', 'かずひろ'],
        ['和幸', 'かずゆき'],
        ['和弘', 'かずひろ'],
        ['和哉', 'かずや'],
        ['和子', 'かずこ'],
        ['和樹', 'かずき'],
        ['和伸', 'かずのぶ'],
        ['和真', 'かずま'],
        ['和人', 'かずひと'],
        ['和生', 'かずお'],
        ['和則', 'かずのり'],
        ['和代', 'かずよ'],
        ['和男', 'かずお'],
        ['和典', 'かずのり'],
        ['和之', 'かずゆき'],
        ['和博', 'かずひろ'],
        ['和美', 'かずみ'],
        ['和彦', 'かずひこ'],
        ['和夫', 'かずお'],
        ['和明', 'かずあき'],
        ['和也', 'かずや'],
        ['和雄', 'かずお'],
        ['亘', 'わたる'],
        ['凛', 'りん'],
        ['惠子', 'けいこ'],
        ['栞', 'しおり'],
        ['栞奈', 'かんな'],
        ['翔', 'かける'],
        ['翔', 'しょう'],
        ['翔子', 'しょうこ'],
        ['翔太', 'しょうた'],
        ['翔大', 'しょうた'],
        ['翔平', 'しょうへい'],
        ['莉奈', 'りな'],
    ]