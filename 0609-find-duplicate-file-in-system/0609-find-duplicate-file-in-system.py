class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = defaultdict(list)
        for path in paths:
            separated_path = path.split(" ")
            directory = separated_path[0]
            for file_info in separated_path[1:]:
                filename, content = file_info.split("(")
                content = content[:-1]   

                full_path = directory + "/" + filename
                content_map[content].append(full_path)

            result = []
            for files in content_map.values():
                if len(files) > 1:
                    result.append(files)
        return result
