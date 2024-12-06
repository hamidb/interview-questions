Design In-Memory File System (Leetcode #588)
===============================
### Hard
 
Design an in-memory file system to simulate the following functions:

`ls`: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is a directory path,
return the list of file and directory names in this directory. Your output (file and directory names together) should in **lexicographic order**.

`mkdir`: Given a directory path that does not exist, you should make a new directory according to the path.
If the middle directories in the path don't exist either, you should create them as well. This function has `void` return type.

`addContentToFile`: Given a file path and file content in string format. If the file doesn't exist,
you need to create that file containing given content. If the file already exists, you need to append given content to original content.
This function has `void` return type.

`readContentFromFile`: Given a file path, return its content in string format.

 
### Example:
```
Input: 
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]

Output:
[null,[],null,null,["a"],"hello"]
```
### Explanation:
![filesystem](https://assets.leetcode.com/uploads/2018/10/12/filesystem.png)

### Note:

* You can assume all file or directory paths are absolute paths which begin with `/` and do not end with `/` except that the path is just `"/"`.
* You can assume that all operations will be passed valid parameters and users will not attempt to retrieve file content or list a directory or file that does not exist.
* You can assume that all directory names and file names only contain lower-case letters, and same names won't exist in the same directory.

Solution
========
More readable
```python
class FileSystemNode:
    def __init__(self):
        self.children = {}  # Directory or file names -> FileSystemNode
        self.content = ""   # Content for files, empty for directories


class FileSystem:
    def __init__(self):
        self.root = FileSystemNode()  # Root directory

    def _traverse(self, path: str) -> FileSystemNode:
        """
        Traverse the file system to the given path.
        """
        current = self.root
        if path == "/":  # Root directory
            return current
        parts = path.split("/")[1:]  # Split path into parts, ignore the leading "/"
        for part in parts:
            if part not in current.children:
                current.children[part] = FileSystemNode()  # Create node if it doesn't exist
            current = current.children[part]
        return current

    def ls(self, path: str) -> list[str]:
        """
        List directory contents or return the file name.
        """
        node = self._traverse(path)
        if node.content:  # It's a file
            return [path.split("/")[-1]]
        # It's a directory, return sorted list of keys in `children`
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        """
        Create directories in the given path.
        """
        self._traverse(path)  # Traverse to the path (creating nodes as needed)

    def addContentToFile(self, filePath: str, content: str) -> None:
        """
        Add content to a file. Create the file if it doesn't exist.
        """
        node = self._traverse(filePath)
        node.content += content  # Append content to the file

    def readContentFromFile(self, filePath: str) -> str:
        """
        Read the content of a file.
        """
        node = self._traverse(filePath)
        return node.content  # Return the file's content

```

```python
# m -> length of path string
# n -> depth of directory
# k -> number of files in directory

# ls: O(m+n+klogk) -> split + traverse + sort
# readContentFromFile, addContentToFile, mkdir: O(m+n) -> split + traverse
class FileSystem:
    class File:
        def __init__(self, is_file=False, content=''):
            self.is_file = is_file
            self.content = content
            self.table = {}  # name -> Files
            
                
    def __init__(self):
        self.root = self.File()  # root is '/'

    def ls(self, path: str) -> List[str]:
        root = self.root
        if path != '/':
            for c in path.split('/'):
                if c == '': continue
                if root.table[c].is_file:
                    return [c]
                root = root.table[c]
        return sorted(root.table.keys())


    def mkdir(self, path: str) -> None:
        if path == '/':
            return
        root = self.root
        for c in path.split('/'):
            if c == '': continue
            if c not in root.table:
                root.table[c] = self.File()
            root = root.table[c]

    def addContentToFile(self, filePath: str, content: str) -> None:
        root = self.root
        for c in filePath.split('/'):
            if c == '': continue
            if c not in root.table:
                root.table[c] = self.File(True, content)
                return
            else:
                if root.table[c].is_file:
                    root.table[c].content += content
                    return
            root = root.table[c]
            
            
    def readContentFromFile(self, filePath: str) -> str:
        root = self.root
        for c in filePath.split('/'):
            if c == '': continue
            root = root.table[c]
        return root.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
```

