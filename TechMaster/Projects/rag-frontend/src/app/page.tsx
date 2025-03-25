'use client';

import { useState, useEffect } from 'react';
import ChatInterface from '@/components/chat/ChatInterface';
import UploadForm from '@/components/document-upload/UploadForm';
import Dashboard from '@/components/dashboard/Dashboard';
import Link from 'next/link';

export default function Home() {
  const [isError, setIsError] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');
  const [isMounted, setIsMounted] = useState(false);

  useEffect(() => {
    setIsMounted(true);
    
    // 전역 에러 핸들러 추가
    const handleError = (event: ErrorEvent) => {
      console.error('클라이언트 오류 감지:', event.error);
      setIsError(true);
      setErrorMessage(event.error?.message || '알 수 없는 오류가 발생했습니다.');
      event.preventDefault();
    };

    window.addEventListener('error', handleError);
    
    return () => {
      window.removeEventListener('error', handleError);
    };
  }, []);

  // 서버 사이드 렌더링 중에는 최소한의 UI만 표시
  if (!isMounted) {
    return <div className="min-h-screen bg-gray-50 py-8" suppressHydrationWarning={true}></div>;
  }
  
  // 에러 발생 시 대체 UI 표시
  if (isError) {
    return (
      <main className="min-h-screen bg-gray-50 py-8" style={{ userSelect: "auto" }} suppressHydrationWarning={true}>
        <div className="container mx-auto px-4" suppressHydrationWarning={true}>
          <div className="bg-red-100 text-red-800 p-6 rounded-lg max-w-2xl mx-auto" suppressHydrationWarning={true}>
            <h1 className="text-2xl font-bold mb-4" suppressHydrationWarning={true}>앱 로딩 중 오류 발생</h1>
            <p className="mb-4" suppressHydrationWarning={true}>{errorMessage}</p>
            <p className="mb-4" suppressHydrationWarning={true}>
              다음 사항을 확인해 보세요:
            </p>
            <ul className="list-disc pl-5 mb-4" suppressHydrationWarning={true}>
              <li suppressHydrationWarning={true}>백엔드 서버가 실행 중인지 확인 (http://localhost:8000)</li>
              <li suppressHydrationWarning={true}>브라우저 콘솔에서 자세한 오류 내용 확인</li>
              <li suppressHydrationWarning={true}>페이지 새로고침</li>
            </ul>
            <button 
              onClick={() => window.location.reload()} 
              className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
              suppressHydrationWarning={true}
            >
              페이지 새로고침
            </button>
          </div>
        </div>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-gray-50 py-8" style={{ userSelect: "auto" }} suppressHydrationWarning={true}>
      <div className="container mx-auto px-4" suppressHydrationWarning={true}>
        <header className="mb-8 text-center" suppressHydrationWarning={true}>
          <h1 className="text-3xl font-bold text-blue-800" suppressHydrationWarning={true}>RAG 시스템 데모</h1>
          <p className="text-gray-600 mt-2" suppressHydrationWarning={true}>
            문서를 업로드하고 질문을 통해 정보를 검색해보세요
          </p>
          <div className="mt-4 flex justify-center space-x-4" suppressHydrationWarning={true}>
            <Link href="/openai-test" className="text-blue-600 hover:text-blue-800 underline" suppressHydrationWarning={true}>
              OpenAI API 테스트 페이지
            </Link>
            <span className="text-gray-300" suppressHydrationWarning={true}>|</span>
            <Link href="/documents" className="text-blue-600 hover:text-blue-800 underline" suppressHydrationWarning={true}>
              참조 문서 관리
            </Link>
          </div>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8" suppressHydrationWarning={true}>
          <div className="md:col-span-1" suppressHydrationWarning={true}>
            <div className="space-y-8" suppressHydrationWarning={true}>
              <UploadForm />
              <Dashboard />
            </div>
          </div>
          
          <div className="md:col-span-2" suppressHydrationWarning={true}>
            <ChatInterface />
          </div>
        </div>
      </div>
    </main>
  );
}