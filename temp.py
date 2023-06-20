def update_results_bbs(results_bbs, valid_mask, new_refboxs):
    # 获取需要更新的元素数量
    update_count = sum(valid_mask)
    # 获取总的参考 box 数量
    N = len(new_refboxs)

    # 判断 results_bbs 长度
    if len(results_bbs) >= (N + 1):
        # 直接用 new_refboxs 里面的元素替换 results_bbs 的最后 N 个元素，new_refboxs顺序读，但是写入results_bbs是倒序写入
        for i in range(N):
            results_bbs[-(i+1)] = new_refboxs[i]
    else:
        # 直接用 new_refboxs 里面的 (update_count - 1) 个元素替换 results_bbs 的最后 N 个元素，new_refboxs顺序读，但是写入results_bbs是倒序写入
        for i in range(update_count-1):
            results_bbs[-(i+1)] = new_refboxs[i]
        
    return results_bbs

def test_update_results_bbs():
    # 测试用例 1 ref0此时是真值不用更新，函数要能够保持result_bbs
    result_bbs_1 = ["ref0"]
    mask_1 = [1, 0, 0]
    new_refboxs_1 = ["box0", "box1", "box2"]
    assert update_results_bbs(result_bbs_1, mask_1, new_refboxs_1) == ["ref0"]

    # 测试用例 2
    result_bbs_2 = ["ref0", "ref1"]
    mask_2 = [1, 1, 0]
    new_refboxs_2 = ["box0", "box1", "box2"]
    assert update_results_bbs(result_bbs_2, mask_2, new_refboxs_2) == ["ref0", "box0"]

    # 测试用例 3
    result_bbs_3 = ["ref0", "ref1", "ref3",]
    mask_3 = [1, 1, 1]
    new_refboxs_3 = ["box0", "box1", "box2"]
    assert update_results_bbs(result_bbs_3, mask_3, new_refboxs_3) == ["ref0", "box1", "box0"]

    # 测试用例 4
    result_bbs_4 = ["ref0", "ref1", "ref3", "ref4"]
    mask_4 = [1, 1, 1]
    new_refboxs_4 = ["box0", "box1", "box2"]
    assert update_results_bbs(result_bbs_4, mask_4, new_refboxs_4) == ["ref0", "box2", "box1", "box0"]

test_update_results_bbs()

# def replace_elements(A, B):
#     # 计算需要替换的元素个数
#     n = len(A)

#     # 从后往前逐个替换B中的元素
#     for i in range(n):
#         B[-(i+1)] = A[i]

#     return B

# # 示例输入
# A = [1, 2, 3]
# B = [4, 5, 6, 7, 8]

# # 替换元素并打印结果
# result = replace_elements(A, B)
# print("替换后的列表B:", result)