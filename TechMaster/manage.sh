#!/bin/bash

BASEDIR=/Users/sangou/TechMaster

function show_help {
    echo "TechMaster 디렉토리 관리 도구"
    echo "사용법: $0 [명령] [인자]"
    echo ""
    echo "명령:"
    echo "  list               - 모든 디렉토리 구조 표시"
    echo "  create DIR         - 새 디렉토리 생성"
    echo "  find KEYWORD       - 키워드로 파일 검색"
    echo "  count              - 각 디렉토리별 파일 수 계산"
    echo "  help               - 도움말 표시"
}

function list_dirs {
    echo "TechMaster 디렉토리 구조:"
    find $BASEDIR -type d -not -path "*/\.*" | sort | sed -e "s|$BASEDIR/||" -e "s|^|  |" -e "s|/|/|g"
}

function create_dir {
    if [ -z "$1" ]; then
        echo "디렉토리 경로를 지정해주세요."
        return 1
    fi
    
    mkdir -p "$BASEDIR/$1"
    echo "디렉토리 생성됨: $BASEDIR/$1"
    echo "# $(basename "$1") 자료" > "$BASEDIR/$1/README.md"
    echo "README.md 파일 생성됨"
}

function find_files {
    if [ -z "$1" ]; then
        echo "검색할 키워드를 입력하세요."
        return 1
    fi
    
    echo "키워드 '$1'로 검색 결과:"
    find $BASEDIR -type f -name "*$1*" | sed "s|$BASEDIR/||"
}

function count_files {
    echo "디렉토리별 파일 수:"
    for dir in $BASEDIR/*; do
        if [ -d "$dir" ]; then
            count=$(find "$dir" -type f | wc -l)
            echo "  $(basename "$dir"): $count 파일"
        fi
    done
}

# 명령 처리
case "$1" in
    list)
        list_dirs
        ;;
    create)
        create_dir "$2"
        ;;
    find)
        find_files "$2"
        ;;
    count)
        count_files
        ;;
    help|*)
        show_help
        ;;
esac 