import glob
import os

## 폴더명 가져오는 함수
def get_folder_title(path):
    # 스크립트 파일이 위치한 폴더의 절대 경로를 얻음
    script_dir = os.path.dirname(path)
    # 폴더명만 추출
    folder_name = os.path.basename(script_dir)

    return folder_name

## .md 파일 경로 가져오는 함수
def find_markdown_files(root_folder):
    markdown_files = {}  # 폴더별 마크다운 파일을 저장할 딕셔너리

    # root_folder 내의 모든 하위 폴더를 순회
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        
        # 폴더인지 확인
        if os.path.isdir(folder_path):
            # 해당 폴더 내의 모든 마크다운 파일 찾기
            files = glob.glob(os.path.join(folder_path, "*.md"))
            
            # 폴더 이름을 키로 하여 파일 리스트 저장
            markdown_files[folder_name] = files

    return markdown_files

## .md 파일 불러오기
def read_markdown_files(folder_path):
    markdown_contents = []

    # 폴더 내의 모든 .md 파일을 찾음
    for md_file in glob.glob(os.path.join(folder_path, "*.md")):
        try:
            with open(md_file, 'r', encoding='utf-8') as file:
                content = file.read()
                markdown_contents.append(content)
        except Exception as e:
            print(f"파일을 읽는 중 오류가 발생했습니다: {e}")

    return markdown_contents