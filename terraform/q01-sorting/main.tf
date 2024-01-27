
locals {
    my_map = {
        "z" = "zoo",
        "b" = "banana",
        "d" = "log"
    }

    my_list = ["banana", "apple", "orange"]
}

output my_list {
    value = local.my_list
}

output my_map {
    value = local.my_map
}

output "sorted_list" {
    value = sort(local.my_list)
}

output sorted_map {
    value = { for key in sort(keys(local.my_map)) : key => local.my_map[key]}
}

output sorted_list_of_keys {
    value = [ for key in sort(keys(local.my_map)): key]
}

output sorted_list_of_values {
    value = [ for key in sort(keys(local.my_map)) : local.my_map[key] ]
}
